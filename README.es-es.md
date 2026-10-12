<p align="center">
  <img src="assets/readme/hero.svg" width="100%" alt="dolphin-finder-noctalia — Dolphin estilo Finder para Hyprland + Noctalia">
</p>

<p align="center"><sub><strong>KDE DOLPHIN · DARKLY · MACTAHOE · HYPRLAND · NOCTALIA</strong></sub></p>

<p align="center">
  <a href="README.md">🇬🇧 English (UK)</a>
  · <a href="README.pt-br.md">🇧🇷 Português (BR)</a>
  · <a href="README.pt-pt.md">🇵🇹 Português (PT)</a>
  · 🇪🇸 <strong>Español (ES)</strong>
  · <a href="README.zh-cn.md">🇨🇳 简体中文</a>
</p>

> Dolphin con aspecto de **Finder de macOS** en **Hyprland + Noctalia**: barra lateral de cristal, iconos **MacTahoe** y carpetas que **cambian de color con el fondo de pantalla**, siguiendo la paleta tonal (Material You) de Noctalia.

<p align="center">
  <img src="screenshots/dolphin.png" width="100%" alt="Dolphin con barra lateral de cristal, iconos MacTahoe y carpetas tonales rosadas">
</p>

---

## 01 / DE UN VISTAZO

<p align="center">
  <img src="assets/readme/at-a-glance.svg" width="100%" alt="Darkly · MacTahoe-dark · Noctalia M3 · Hyprland">
</p>

## 02 / CAPACIDADES

<p align="center">
  <img src="assets/readme/capabilities.svg" width="100%" alt="CAPACIDADES">
</p>

| Pieza | Qué hace |
|---|---|
| **Darkly** (estilo Qt6) | Esquinas redondeadas; barra lateral y barra de herramientas translúcidas, cristal sutil en el área de archivos; sin línea de foco ni separadores |
| **MacTahoe-dark** (iconos) | Iconos al estilo macOS Tahoe |
| **Plantilla de Noctalia** + `mactahoe-recolor.py` | Cada vez que cambia el esquema, pinta las carpetas con el tono principal de Noctalia |
| **dolphinrc / dolphinui.rc** | Sin menú, barra de herramientas mínima (◀ ▶ · vista · ruta · búsqueda · terminal · menú), control de zoom, iconos de 64 px |
| **Iconos de carpetas** (`config/folder-icons.tsv`) | Iconos personalizados por carpeta (p. ej. `Vault → folder-sign`) |
| **Reglas de Hyprland** (`hypr/dolphin.lua`) | Ventana opaca (el cristal lo pone Darkly) y diálogos flotantes |

### ¿Qué ocurre por debajo?

- La translucidez la dibuja **Darkly**, widget a widget. Hyprland mantiene la ventana en `opacity 1.0` y solo aplica desenfoque donde Darkly deja ver.
- Noctalia genera `palette.json` a partir de su esquema M3 en cada cambio de fondo/esquema y ejecuta el `post_hook`.
- El hook reescribe los 18 SVG de carpetas en `places/scalable` a partir de los originales azules (`#006efd`) y vacía la caché de iconos de KDE.

## 03 / CANAL TONAL

<p align="center">
  <img src="assets/readme/tonal-pipeline.svg" width="100%" alt="wallpaper → M3 → palette.json → mactahoe-recolor.py → icons">
</p>

El matiz sale de `primary.light`, la saturación del más vivo de los dos primarios (con tope en `MAX_SAT`) y la luminosidad es fija (`LIGHTNESS`). La carpeta conserva el matiz del fondo sin volverse neón ni desvaída.

## 04 / INSTALACIÓN

### Requisitos

- Arch / CachyOS (usa `paru` o `yay`)
- Hyprland (configuración en Lua) con desenfoque activado
- Noctalia Shell con las plantillas `qt` y `kcolorscheme` activas
- `qt6ct` como platform theme (`QT_QPA_PLATFORMTHEME=qt6ct`)
- `fish`, `git`, `python3`, `kwriteconfig6`

### Vía rápida

```fish
git clone https://github.com/mastermaiolo/dolphin-finder-noctalia.git
cd dolphin-finder-noctalia
./install.fish
```

<details>
<summary><strong>Qué hace el instalador</strong></summary>

1. instala `darkly`, `inter-font`, `git` y `python` (se omite con `--no-deps`);
2. clona [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) y lo instala en `~/.local/share/icons`;
3. copia la plantilla y el script de recoloreado a `~/.config/noctalia/` y registra la plantilla en `config.toml`;
4. aplica `darklyrc`, `qt6ct` (Darkly + MacTahoe-dark), `dolphinrc`, la barra de herramientas y los iconos de carpetas.

Antes de tocar un fichero siempre hace una copia (`*.bak-AAAAMMDD-HHMMSS`).

</details>

### Pasos manuales

- copia las reglas de [`hypr/dolphin.lua`](hypr/dolphin.lua) a tu configuración de Hyprland;
- usa `scale >= 1` en el monitor (ver *08 / Problemas conocidos*);
- en qt6ct, elige la fuente **Inter 10**;
- cierra y vuelve a abrir Dolphin.

## 05 / SUPERFICIE DE CONTROL

<p align="center">
  <img src="assets/readme/control-surface.svg" width="100%" alt="LIGHTNESS · MAX_SAT · darklyrc">
</p>

Para aplicar el recoloreado al momento:

```fish
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py            # color de Noctalia
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py '#1a8fe8'  # color fijo
```

## 06 / CONFIGURACIÓN

**Color de las carpetas:** al principio de `~/.config/noctalia/scripts/mactahoe-recolor.py`.

```python
LIGHTNESS = 0.58   # más bajo = carpeta más oscura (Finder ≈ 0.50)
MAX_SAT   = 0.60   # 0.3 = tonal discreto · 0.8 = vivo
```

**Cristal:** en `~/.config/darklyrc`.

| Clave | Valor | Efecto |
|---|---|---|
| `DolphinSidebarOpacity` | 55 | barra lateral (40 = más cristal, 70 = más sólida) |
| `ToolBarOpacity` | 55 | barra de herramientas |
| `DolphinViewOpacity` | 80 | área de archivos (súbelo a 85–90 con fondos claros) |

<details>
<summary><strong>Bloque de plantilla de Noctalia</strong></summary>

Añadido a `~/.config/noctalia/config.toml` por `install.fish` (o a mano desde `noctalia/config.snippet.toml`):

```toml
[theme.templates.user.mactahoe]
input_path = "$HOME/.config/noctalia/templates/mactahoe/palette.json"
output_path = "$HOME/.local/state/mactahoe-noctalia/palette.json"
post_hook = "python3 $HOME/.config/noctalia/scripts/mactahoe-recolor.py"
```

</details>

## 07 / ARQUITECTURA

<p align="center">
  <img src="assets/readme/architecture.svg" width="100%" alt="ARQUITECTURA">
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
├── assets/readme/          # ilustraciones del README
└── screenshots/
```

## 08 / PROBLEMAS CONOCIDOS

<p align="center">
  <img src="assets/readme/failure-modes.svg" width="100%" alt="PROBLEMAS CONOCIDOS">
</p>

<details>
<summary><strong>Notas detalladas</strong></summary>

- **Desenfoque cortado abajo o a la derecha de la ventana:** ocurre con un `scale` del monitor inferior a 1 (p. ej. `0.9375`). Hyprland recorta el desenfoque en `ancho×scale` / `alto×scale`. Solución: `scale = "1"`.
- **Barras de capacidad en los dispositivos** de la barra lateral: Dolphin no tiene opción para ocultarlas.
- **"16 folders" en inglés** en la barra de estado: son textos que aún no están traducidos en el propio Dolphin.
- **Las carpetas no cambian de color:** el `post_hook` no se ejecutó o falta `python3` — ejecuta `mactahoe-recolor.py` a mano.
- **Reinstalar MacTahoe** puede mostrar avisos `cannot remove`: son inofensivos.

</details>

<details>
<summary><strong>Apéndice — desinstalar</strong></summary>

```fish
rm -rf ~/.local/share/icons/MacTahoe{,-dark,-light} ~/.local/share/mactahoe-noctalia
rm ~/.config/noctalia/scripts/mactahoe-recolor.py
rm -r ~/.config/noctalia/templates/mactahoe
```

Después:

- elimina el bloque `[theme.templates.user.mactahoe]` del `config.toml` de Noctalia;
- restaura los `*.bak-*` que quieras.

</details>

## 09 / PROCEDENCIA

<p align="center">
  <img src="assets/readme/provenance.svg" width="100%" alt="MacTahoe · Darkly · Noctalia · MIT">
</p>

- [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme), de vinceliuice — se descarga durante la instalación, no se incluye aquí.
- [Darkly](https://github.com/Bali10050/Darkly) — estilo Qt.
- [Noctalia](https://noctalia.dev) — shell y motor de plantillas.

## 10 / LICENCIA

- Scripts y configuraciones de este repositorio: [MIT](LICENSE).
- MacTahoe-icon-theme: GPL-3.0 (licencia del proyecto original).

---

<p align="center"><sub>MAIOLO / SYSTEMS LAB · DFN</sub></p>
