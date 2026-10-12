<p align="center">
  <img src="assets/readme/hero.svg" width="100%" alt="dolphin-finder-noctalia — a Finder-style Dolphin for Hyprland + Noctalia">
</p>

<p align="center"><sub><strong>KDE DOLPHIN · DARKLY · MACTAHOE · HYPRLAND · NOCTALIA</strong></sub></p>

<p align="center">
  🇬🇧 <strong>English (UK)</strong>
  · <a href="README.pt-br.md">🇧🇷 Português (BR)</a>
  · <a href="README.pt-pt.md">🇵🇹 Português (PT)</a>
  · <a href="README.es-es.md">🇪🇸 Español (ES)</a>
  · <a href="README.zh-cn.md">🇨🇳 简体中文</a>
</p>

> Dolphin restyled as a **macOS Finder** on **Hyprland + Noctalia**: a glass sidebar, **MacTahoe** icons and folders that **change colour with the wallpaper**, following Noctalia's tonal (Material You) palette.

<p align="center">
  <img src="screenshots/dolphin.png" width="100%" alt="Dolphin with a glass sidebar, MacTahoe icons and rose tonal folders">
</p>

---

## 01 / AT A GLANCE

<p align="center">
  <img src="assets/readme/at-a-glance.svg" width="100%" alt="Darkly · MacTahoe-dark · Noctalia M3 · Hyprland">
</p>

## 02 / CAPABILITIES

<p align="center">
  <img src="assets/readme/capabilities.svg" width="100%" alt="CAPABILITIES">
</p>

| Piece | What it does |
|---|---|
| **Darkly** (Qt6 style) | Rounded corners; translucent sidebar and toolbar, subtle glass on the file area; no focus line, no separators |
| **MacTahoe-dark** (icons) | macOS Tahoe–style icons |
| **Noctalia template** + `mactahoe-recolor.py` | Whenever the scheme changes, paints the folders with Noctalia's primary tone |
| **dolphinrc / dolphinui.rc** | No menu bar, minimal toolbar (◀ ▶ · view · path · search · terminal · menu), zoom slider, 64 px icons |
| **Folder icons** (`config/folder-icons.tsv`) | Custom icons per folder (e.g. `Vault → folder-sign`) |
| **Hyprland rules** (`hypr/dolphin.lua`) | Opaque window (the glass comes from Darkly) and floating dialogs |

### What is actually happening?

- The translucency is drawn by **Darkly**, per widget. Hyprland keeps the window at `opacity 1.0` and blurs only what Darkly leaves see-through.
- Noctalia renders `palette.json` from its M3 scheme on every wallpaper/scheme change, then runs the `post_hook`.
- The hook rewrites the 18 folder SVGs in `places/scalable` from pristine blue originals (`#006efd`), then clears the KDE icon cache.

## 03 / TONAL PIPELINE

<p align="center">
  <img src="assets/readme/tonal-pipeline.svg" width="100%" alt="wallpaper → M3 → palette.json → mactahoe-recolor.py → icons">
</p>

The hue comes from `primary.light`, the saturation from the more vivid of the two primaries (capped at `MAX_SAT`), and the lightness is fixed (`LIGHTNESS`). The folder keeps the wallpaper's hue without turning neon or washed out.

## 04 / INSTALL

### Requirements

- Arch / CachyOS (uses `paru` or `yay`)
- Hyprland (Lua config) with blur enabled
- Noctalia Shell with the `qt` and `kcolorscheme` templates active
- `qt6ct` as the platform theme (`QT_QPA_PLATFORMTHEME=qt6ct`)
- `fish`, `git`, `python3`, `kwriteconfig6`

### Fast path

```fish
git clone https://github.com/mastermaiolo/dolphin-finder-noctalia.git
cd dolphin-finder-noctalia
./install.fish
```

<details>
<summary><strong>What the installer does</strong></summary>

1. installs `darkly`, `inter-font`, `git` and `python` (skip with `--no-deps`);
2. clones [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) and installs it into `~/.local/share/icons`;
3. copies the template and the recolour script into `~/.config/noctalia/` and registers the template in `config.toml`;
4. applies `darklyrc`, `qt6ct` (Darkly + MacTahoe-dark), `dolphinrc`, the toolbar and the folder icons.

Every file it touches is backed up first (`*.bak-YYYYMMDD-HHMMSS`).

</details>

### Manual steps

- copy the rules from [`hypr/dolphin.lua`](hypr/dolphin.lua) into your Hyprland config;
- use `scale >= 1` on the monitor (see *08 / Failure modes*);
- in qt6ct, pick the **Inter 10** font;
- close and reopen Dolphin.

## 05 / CONTROL SURFACE

<p align="center">
  <img src="assets/readme/control-surface.svg" width="100%" alt="LIGHTNESS · MAX_SAT · darklyrc">
</p>

Apply the recolour immediately:

```fish
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py            # Noctalia colour
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py '#1a8fe8'  # fixed colour
```

## 06 / CONFIGURATION

**Folder colour:** at the top of `~/.config/noctalia/scripts/mactahoe-recolor.py`.

```python
LIGHTNESS = 0.58   # lower = darker folder (Finder ≈ 0.50)
MAX_SAT   = 0.60   # 0.3 = discreet tonal · 0.8 = vivid
```

**Glass:** in `~/.config/darklyrc`.

| Key | Value | Effect |
|---|---|---|
| `DolphinSidebarOpacity` | 55 | sidebar (40 = glassier, 70 = more solid) |
| `ToolBarOpacity` | 55 | toolbar |
| `DolphinViewOpacity` | 80 | file area (raise to 85–90 with light wallpapers) |

<details>
<summary><strong>Noctalia template block</strong></summary>

Added to `~/.config/noctalia/config.toml` by `install.fish` (or by hand from `noctalia/config.snippet.toml`):

```toml
[theme.templates.user.mactahoe]
input_path = "$HOME/.config/noctalia/templates/mactahoe/palette.json"
output_path = "$HOME/.local/state/mactahoe-noctalia/palette.json"
post_hook = "python3 $HOME/.config/noctalia/scripts/mactahoe-recolor.py"
```

</details>

## 07 / ARCHITECTURE

<p align="center">
  <img src="assets/readme/architecture.svg" width="100%" alt="ARCHITECTURE">
</p>

```text
dolphin-finder-noctalia/
├── install.fish
├── config/
│   ├── darklyrc
│   └── folder-icons.tsv
├── hypr/
│   └── dolphin.lua
├── kxmlgui/
│   └── dolphinui.rc
├── noctalia/
│   ├── config.snippet.toml
│   ├── scripts/mactahoe-recolor.py
│   └── templates/mactahoe/palette.json
├── assets/readme/          # README artwork
└── screenshots/
```

## 08 / FAILURE MODES

<p align="center">
  <img src="assets/readme/failure-modes.svg" width="100%" alt="FAILURE MODES">
</p>

<details>
<summary><strong>Long-form notes</strong></summary>

- **Blur cut off at the bottom or right of the window:** happens with a monitor `scale` below 1 (e.g. `0.9375`). Hyprland clips the blur at `width×scale` / `height×scale`. Fix: `scale = "1"`.
- **Capacity bars on the devices** in the sidebar: Dolphin has no option to hide them.
- **"16 folders" in English** in the status bar: these strings are not yet translated in Dolphin itself.
- **Folders keep their old colour:** the `post_hook` did not run or `python3` is missing — run `mactahoe-recolor.py` by hand.
- **Reinstalling MacTahoe** may print `cannot remove` warnings: they are harmless.

</details>

<details>
<summary><strong>Appendix — uninstall</strong></summary>

```fish
rm -rf ~/.local/share/icons/MacTahoe{,-dark,-light} ~/.local/share/mactahoe-noctalia
rm ~/.config/noctalia/scripts/mactahoe-recolor.py
rm -r ~/.config/noctalia/templates/mactahoe
```

Then:

- remove the `[theme.templates.user.mactahoe]` block from Noctalia's `config.toml`;
- restore whichever `*.bak-*` files you want.

</details>

## 09 / PROVENANCE

<p align="center">
  <img src="assets/readme/provenance.svg" width="100%" alt="MacTahoe · Darkly · Noctalia · MIT">
</p>

- [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) by vinceliuice — downloaded at install time, not bundled here.
- [Darkly](https://github.com/Bali10050/Darkly) — Qt style.
- [Noctalia](https://noctalia.dev) — shell and template engine.

## 10 / LICENCE

- Scripts and configs in this repository: [MIT](LICENSE).
- MacTahoe-icon-theme: GPL-3.0 (upstream licence).

---

<p align="center"><sub>MAIOLO / SYSTEMS LAB · DFN</sub></p>
