# AI 3D Benchmarks

A collection of **14 single-file AI benchmark builds** (procedural Three.js 3D scenes & interactive web OS demos) running live at **60 FPS** directly in the browser — built with **no external 3D models, image textures, or build steps**.

- **Live Fullscreen Showcase (auto-plays immediately):** https://vsrikanth05.github.io/ai-3d-benchmarks/

## Playable 3D Scenes

Opening the showcase URL above plays **Chandrayaan-3 Landing** fullscreen right away, with a subtle bottom-right scene switcher to browse all 14 builds, replay, or jump to any standalone no-UI file.

| # | Scene | Showcase Link | Direct Standalone (No UI) | Source |
|---|---|---|---|---|
| 1 | **Chandrayaan-3 Lunar South Pole Landing** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=chandrayaan-3-landing) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/chandrayaan-3-landing.html) | [`chandrayaan-3-landing.html`](./chandrayaan-3-landing.html) |
| 2 | **SpaceX Starship Launch** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=spacex-starship-launch) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/spacex-starship-launch.html) | [`spacex-starship-launch.html`](./spacex-starship-launch.html) |
| 3 | **SpaceX Starship Belly-Flop Landing** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=spacex-starship-landing) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/spacex-starship-landing.html) | [`spacex-starship-landing.html`](./spacex-starship-landing.html) |
| 4 | **Mysore Palace — Dasara Night** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=mysore-palace-dasara) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/mysore-palace-dasara.html) | [`mysore-palace-dasara.html`](./mysore-palace-dasara.html) |
| 5 | **Grandmaster's Study — 3D Chess** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=chess-grandmaster-study) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/chess-grandmaster-study.html) | [`chess-grandmaster-study.html`](./chess-grandmaster-study.html) |
| 6 | **F1 Four-Car Grand Prix** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=f1-four-car-race) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/f1-four-car-race.html) | [`f1-four-car-race.html`](./f1-four-car-race.html) |
| 7 | **Red & Black Hypercar** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=red-black-hypercar) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/red-black-hypercar.html) | [`red-black-hypercar.html`](./red-black-hypercar.html) |
| 8 | **Pagoda Bridge Gate** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=pagoda-bridge-gate) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/pagoda-bridge-gate.html) | [`pagoda-bridge-gate.html`](./pagoda-bridge-gate.html) |
| 9 | **Tropical Coast City** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=tropical-coast-city) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/tropical-coast-city.html) | [`tropical-coast-city.html`](./tropical-coast-city.html) |
| 10 | **Snowy Log Cabin Diorama** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=snowy-cabin-diorama) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/snowy-cabin-diorama.html) | [`snowy-cabin-diorama.html`](./snowy-cabin-diorama.html) |
| 11 | **Supermassive Black Hole** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=supermassive-black-hole) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/supermassive-black-hole.html) | [`supermassive-black-hole.html`](./supermassive-black-hole.html) |
| 12 | **Coffee Ghost** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=coffee-ghost) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/coffee-ghost.html) | [`coffee-ghost.html`](./coffee-ghost.html) |
| 13 | **Sci-Fi Galaxy Hologram** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=07-galaxy-hologram) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/07-galaxy-hologram.html) | [`07-galaxy-hologram.html`](./07-galaxy-hologram.html) |
| 14 | **macOS Sequoia — Interactive Desktop (Gemini 4 Neon)** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=macos-sequoia-desktop) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/macos_sequoia_interactive_desktop.html) | [`macos_sequoia_interactive_desktop.html`](./macos_sequoia_interactive_desktop.html) |
| 15 | **Jensen Huang: The 11-Day Comeback (Arcade Game — Gemini 4 Neon)** | [Play](https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=jensen-huang-11-day-comeback) | [Standalone](https://vsrikanth05.github.io/ai-3d-benchmarks/jensen-huang-11-day-comeback.html) | [`jensen-huang-11-day-comeback.html`](./jensen-huang-11-day-comeback.html) |

## Tools & Tech Stack Used

### 3D Rendering & Procedural Generation
- **[Three.js](https://threejs.org/) (`v0.170.0`)** via native ES module `<script type="importmap">` (zero bundler required)
- **WebGL2 + Custom GLSL Shaders** for vacuum thruster plumes, atmospheric limb scattering, low-gravity dust particles, and volumetric effects
- **Procedural Canvas PBR Maps** generating seamless albedo, Sobel-derived normal, and roughness maps entirely in JavaScript (crinkled Kapton gold foil, aluminized Mylar, brushed aluminum, photovoltaic solar arrays, lunar regolith, wheel-track imprints)
- **Procedural HDR Lighting & Post-Processing** via `PMREMGenerator`, `PCFSoftShadowMap` (`4096×4096`), `EffectComposer`, `UnrealBloomPass`, and `ACESFilmicToneMapping`

### Deterministic 60 FPS Video Capture Pipeline (`tools/`)
- **[`tools/record_scene.py`](./tools/record_scene.py)** — Reusable Python script using **Playwright** + headless **Chromium (ANGLE/D3D11 WebGL)** + **Chrome DevTools Protocol (`Page.captureScreenshot`)** + **FFmpeg** (`libx264`, `yuv420p`, `+faststart`)
- Injects a deterministic virtual `requestAnimationFrame` / `performance.now` clock so every frame renders at exact `1/60s` intervals with **zero dropped frames** regardless of GPU render load.

### Hosting & Showcase
- **GitHub Pages** static hosting with [`index.html`](./index.html) fullscreen player and [`scenes.json`](./scenes.json) manifest.

## Local Preview & Recording

### Run Locally
```bash
python -m http.server 8765
# Open http://localhost:8765/
```

### Record Any Scene to 1080p 60 FPS MP4
Requires Python 3.10+, [FFmpeg](https://ffmpeg.org/) on `PATH`, and Playwright Chromium:

```bash
pip install -r tools/requirements.txt
playwright install chromium

python tools/record_scene.py chandrayaan-3-landing.html out/chandrayaan-3-landing.mp4 --duration 27.5 --fps 60
```

## Adding More 3D Scenes

1. Drop your standalone `.html` scene file into the repository root.
2. Add an entry to [`scenes.json`](./scenes.json) (index `0` is the default auto-playing scene when opening the root URL).
