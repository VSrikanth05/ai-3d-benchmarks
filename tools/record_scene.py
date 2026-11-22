"""
Deterministic 60 FPS WebGL/Three.js Scene Recorder
--------------------------------------------------
Captures any standalone HTML Three.js scene in this repository at exact virtual-clock
frame intervals (zero dropped frames, zero stutter) using Playwright + Chromium GPU
WebGL (ANGLE/D3D11) and pipes lossless PNG frames directly into FFmpeg H.264 MP4.

Usage:
    python tools/record_scene.py chandrayaan-3-landing.html out.mp4
    python tools/record_scene.py chandrayaan-3-landing.html out.mp4 --duration 27.5 --fps 60 --width 1920 --height 1080
"""

import argparse
import base64
import os
import subprocess
import sys
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from playwright.sync_api import sync_playwright

INIT_SCRIPT = """
(() => {
  // Deterministic virtual clock so requestAnimationFrame advances at exact 1/FPS steps
  let virtualNow = 0;
  performance.now = () => virtualNow;

  let nextId = 1;
  const rafQueue = new Map();
  window.requestAnimationFrame = (cb) => {
    const id = nextId++;
    rafQueue.set(id, cb);
    return id;
  };
  window.cancelAnimationFrame = (id) => {
    rafQueue.delete(id);
  };

  window.__advanceFrame = (dtMs) => {
    virtualNow += dtMs;
    const current = Array.from(rafQueue.entries());
    rafQueue.clear();
    for (const [, cb] of current) {
      cb(virtualNow);
    }
  };
})();
"""


def start_static_server(directory: str, port: int) -> ThreadingHTTPServer:
    class QuietHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

        def log_message(self, fmt, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", port), QuietHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def record_scene(
    html_file: str,
    out_video: str,
    width: int = 1920,
    height: int = 1080,
    fps: int = 60,
    duration: float = 27.5,
    crf: int = 16,
    port: int = 8766,
) -> None:
    html_path = os.path.abspath(html_file)
    if not os.path.isfile(html_path):
        raise FileNotFoundError(f"Scene HTML file not found: {html_path}")

    serve_dir = os.path.dirname(html_path)
    filename = os.path.basename(html_path)
    total_frames = int(round(fps * duration))

    out_abs = os.path.abspath(out_video)
    os.makedirs(os.path.dirname(out_abs), exist_ok=True)

    server = start_static_server(serve_dir, port)
    print(f"Serving {serve_dir} on http://127.0.0.1:{port}/{filename}", flush=True)

    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-f", "image2pipe",
        "-vcodec", "png",
        "-framerate", str(fps),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", str(crf),
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        out_abs,
    ]

    ff = subprocess.Popen(
        ffmpeg_cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--use-gl=angle",
                    "--use-angle=d3d11",
                    "--enable-webgl",
                    "--ignore-gpu-blocklist",
                    "--disable-gpu-vsync",
                    "--no-sandbox",
                ],
            )
            context = browser.new_context(
                viewport={"width": width, "height": height},
                device_scale_factor=1,
            )
            page = context.new_page()
            page.add_init_script(INIT_SCRIPT)

            console_errors = []
            page.on("pageerror", lambda err: console_errors.append(str(err)))
            page.on(
                "console",
                lambda msg: console_errors.append(msg.text) if msg.type == "error" else None,
            )

            page.goto(f"http://127.0.0.1:{port}/{filename}", wait_until="networkidle", timeout=60000)
            page.wait_for_selector("canvas", timeout=30000)
            page.evaluate("window.__advanceFrame(0)")
            time.sleep(0.5)

            cdp = context.new_cdp_session(page)
            dt_ms = 1000.0 / fps
            t0 = time.time()

            for frame in range(total_frames):
                if frame > 0:
                    page.evaluate(f"window.__advanceFrame({dt_ms})")
                res = cdp.send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
                ff.stdin.write(base64.b64decode(res["data"]))

                if frame % 120 == 0 or frame == total_frames - 1:
                    elapsed = time.time() - t0
                    cap_fps = (frame + 1) / max(elapsed, 0.001)
                    print(
                        f"Frame {frame + 1}/{total_frames} ({(frame + 1) / fps:.2f}s) | "
                        f"capture: {cap_fps:.1f} fps | elapsed: {elapsed:.1f}s",
                        flush=True,
                    )

            browser.close()
            if console_errors:
                print("Console errors:", console_errors, flush=True)
    finally:
        if ff.stdin:
            ff.stdin.close()
        _, err = ff.communicate()
        server.shutdown()
        if ff.returncode != 0:
            print("FFmpeg error:", err.decode("utf-8", errors="ignore"), flush=True)
            sys.exit(1)

    size_mb = os.path.getsize(out_abs) / (1024 * 1024)
    print(f"Saved {out_abs} ({size_mb:.2f} MB)", flush=True)


def main():
    parser = argparse.ArgumentParser(description="Record a Three.js HTML scene to 60 FPS MP4.")
    parser.add_argument("html_file", help="Path to standalone HTML scene file")
    parser.add_argument("out_video", help="Destination MP4 file path")
    parser.add_argument("--width", type=int, default=1920, help="Viewport width (default: 1920)")
    parser.add_argument("--height", type=int, default=1080, help="Viewport height (default: 1080)")
    parser.add_argument("--fps", type=int, default=60, help="Target FPS (default: 60)")
    parser.add_argument("--duration", type=float, default=27.5, help="Duration in seconds (default: 27.5)")
    parser.add_argument("--crf", type=int, default=16, help="FFmpeg H.264 CRF quality (default: 16)")
    parser.add_argument("--port", type=int, default=8766, help="Local HTTP server port (default: 8766)")
    args = parser.parse_args()

    record_scene(
        html_file=args.html_file,
        out_video=args.out_video,
        width=args.width,
        height=args.height,
        fps=args.fps,
        duration=args.duration,
        crf=args.crf,
        port=args.port,
    )


if __name__ == "__main__":
    main()
