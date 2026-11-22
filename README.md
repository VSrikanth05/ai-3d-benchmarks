# AI 3D Benchmarks

Single-file procedural Three.js scenes running live at 60 FPS in the browser — built purely from analytic geometry and code with no external assets.

- **Live Showcase (auto-plays fullscreen immediately):** https://vsrikanth05.github.io/ai-3d-benchmarks/

## Scenes

| Scene | Direct Live 60 FPS URL | Source |
|---|---|---|
| **Chandrayaan-3 Landing** | [Launch](https://vsrikanth05.github.io/ai-3d-benchmarks/chandrayaan-3-landing.html) | [`chandrayaan-3-landing.html`](./chandrayaan-3-landing.html) |

## Adding a New 3D Scene

1. Add your standalone `.html` file to the root of this repository.
2. Add one entry to [`scenes.json`](./scenes.json) (put it first if you want it to auto-play by default on the root URL):

```json
{
  "id": "my-scene",
  "title": "My 3D Scene",
  "file": "my-scene.html",
  "description": "Short description of the scene."
}
```

You can also link directly to any scene inside the showcase with `?scene=<id>` (e.g., `https://vsrikanth05.github.io/ai-3d-benchmarks/?scene=chandrayaan-3-landing`) or standalone without the corner switcher via `/<file>.html`.
