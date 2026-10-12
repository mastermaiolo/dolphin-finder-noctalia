# Fonte dos textos dos READMEs. Edita aqui e corre:  python3 lang.py && python3 build.py
import json
L = {
 "en": {
  "alt_hero": "a Finder-style Dolphin for Hyprland + Noctalia",
  "lead": "Dolphin restyled as a **macOS Finder** on **Hyprland + Noctalia**: a glass sidebar, **MacTahoe** icons and folders that **change colour with the wallpaper**, following Noctalia's tonal (Material You) palette.",
  "alt_shot": "Dolphin with a glass sidebar, MacTahoe icons and rose tonal folders",
  "h": [
   "AT A GLANCE",
   "CAPABILITIES",
   "TONAL PIPELINE",
   "INSTALL",
   "CONTROL SURFACE",
   "CONFIGURATION",
   "ARCHITECTURE",
   "FAILURE MODES",
   "PROVENANCE",
   "LICENCE"
  ],
  "th": [
   "Piece",
   "What it does"
  ],
  "pieces": [
   [
    "**Darkly** (Qt6 style)",
    "Rounded corners; translucent sidebar and toolbar, subtle glass on the file area; no focus line, no separators"
   ],
   [
    "**MacTahoe-dark** (icons)",
    "macOS Tahoe–style icons"
   ],
   [
    "**Noctalia template** + `mactahoe-recolor.py`",
    "Whenever the scheme changes, paints the folders with Noctalia's primary tone"
   ],
   [
    "**dolphinrc / dolphinui.rc**",
    "No menu bar, minimal toolbar (◀ ▶ · view · path · search · terminal · menu), zoom slider, 64 px icons"
   ],
   [
    "**Folder icons** (`config/folder-icons.tsv`)",
    "Custom icons per folder (e.g. `Vault → folder-sign`)"
   ],
   [
    "**Hyprland rules** (`hypr/dolphin.lua`)",
    "Opaque window (the glass comes from Darkly) and floating dialogs"
   ]
  ],
  "what": "What is actually happening?",
  "happen": [
   "The translucency is drawn by **Darkly**, per widget. Hyprland keeps the window at `opacity 1.0` and blurs only what Darkly leaves see-through.",
   "Noctalia renders `palette.json` from its M3 scheme on every wallpaper/scheme change, then runs the `post_hook`.",
   "The hook rewrites the 18 folder SVGs in `places/scalable` from pristine blue originals (`#006efd`), then clears the KDE icon cache."
  ],
  "pipe": "The hue comes from `primary.light`, the saturation from the more vivid of the two primaries (capped at `MAX_SAT`), and the lightness is fixed (`LIGHTNESS`). The folder keeps the wallpaper's hue without turning neon or washed out.",
  "req_h": "Requirements",
  "req": [
   "Arch / CachyOS (uses `paru` or `yay`)",
   "Hyprland (Lua config) with blur enabled",
   "Noctalia Shell with the `qt` and `kcolorscheme` templates active",
   "`qt6ct` as the platform theme (`QT_QPA_PLATFORMTHEME=qt6ct`)",
   "`fish`, `git`, `python3`, `kwriteconfig6`"
  ],
  "fast": "Fast path",
  "user": "mastermaiolo",
  "inst_h": "What the installer does",
  "inst": [
   "installs `darkly`, `inter-font`, `git` and `python` (skip with `--no-deps`);",
   "clones [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) and installs it into `~/.local/share/icons`;",
   "copies the template and the recolour script into `~/.config/noctalia/` and registers the template in `config.toml`;",
   "applies `darklyrc`, `qt6ct` (Darkly + MacTahoe-dark), `dolphinrc`, the toolbar and the folder icons."
  ],
  "backup": "Every file it touches is backed up first (`*.bak-YYYYMMDD-HHMMSS`).",
  "manual_h": "Manual steps",
  "manual": [
   "copy the rules from [`hypr/dolphin.lua`](hypr/dolphin.lua) into your Hyprland config;",
   "use `scale >= 1` on the monitor (see *08 / Failure modes*);",
   "in qt6ct, pick the **Inter 10** font;",
   "close and reopen Dolphin."
  ],
  "now": "Apply the recolour immediately:",
  "c_noct": "Noctalia colour",
  "c_fixed": "fixed colour",
  "fc": "**Folder colour:** at the top of `~/.config/noctalia/scripts/mactahoe-recolor.py`.",
  "py_l": "lower = darker folder (Finder ≈ 0.50)",
  "py_s": "0.3 = discreet tonal · 0.8 = vivid",
  "gl": "**Glass:** in `~/.config/darklyrc`.",
  "gth": [
   "Key",
   "Value",
   "Effect"
  ],
  "glass": [
   [
    "DolphinSidebarOpacity",
    "55",
    "sidebar (40 = glassier, 70 = more solid)"
   ],
   [
    "ToolBarOpacity",
    "55",
    "toolbar"
   ],
   [
    "DolphinViewOpacity",
    "80",
    "file area (raise to 85–90 with light wallpapers)"
   ]
  ],
  "tb_h": "Noctalia template block",
  "tb": "Added to `~/.config/noctalia/config.toml` by `install.fish` (or by hand from `noctalia/config.snippet.toml`):",
  "art": "README artwork",
  "long": "Long-form notes",
  "fail": [
   "**Blur cut off at the bottom or right of the window:** happens with a monitor `scale` below 1 (e.g. `0.9375`). Hyprland clips the blur at `width×scale` / `height×scale`. Fix: `scale = \"1\"`.",
   "**Capacity bars on the devices** in the sidebar: Dolphin has no option to hide them.",
   "**\"16 folders\" in English** in the status bar: these strings are not yet translated in Dolphin itself.",
   "**Folders keep their old colour:** the `post_hook` did not run or `python3` is missing — run `mactahoe-recolor.py` by hand.",
   "**Reinstalling MacTahoe** may print `cannot remove` warnings: they are harmless."
  ],
  "un_h": "Appendix — uninstall",
  "then": "Then:",
  "un": [
   "remove the `[theme.templates.user.mactahoe]` block from Noctalia's `config.toml`;",
   "restore whichever `*.bak-*` files you want."
  ],
  "prov": [
   "[MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) by vinceliuice — downloaded at install time, not bundled here.",
   "[Darkly](https://github.com/Bali10050/Darkly) — Qt style.",
   "[Noctalia](https://noctalia.dev) — shell and template engine."
  ],
  "lic": [
   "Scripts and configs in this repository: [MIT](LICENSE).",
   "MacTahoe-icon-theme: GPL-3.0 (upstream licence)."
  ]
 },
 "pt-pt": {
  "alt_hero": "Dolphin estilo Finder para Hyprland + Noctalia",
  "lead": "Dolphin com cara de **Finder do macOS** em **Hyprland + Noctalia**: barra lateral de vidro, ícones **MacTahoe** e pastas que **mudam de cor com o wallpaper**, seguindo a paleta tonal (Material You) do Noctalia.",
  "alt_shot": "Dolphin com barra lateral de vidro, ícones MacTahoe e pastas tonais cor-de-rosa",
  "h": [
   "VISÃO GERAL",
   "CAPACIDADES",
   "PIPELINE TONAL",
   "INSTALAÇÃO",
   "SUPERFÍCIE DE CONTROLO",
   "CONFIGURAÇÃO",
   "ARQUITETURA",
   "PROBLEMAS CONHECIDOS",
   "PROVENIÊNCIA",
   "LICENÇA"
  ],
  "th": [
   "Peça",
   "O que faz"
  ],
  "pieces": [
   [
    "**Darkly** (estilo Qt6)",
    "Cantos arredondados; barra lateral e toolbar translúcidas, vidro subtil na área das pastas; sem linha de foco nem separadores"
   ],
   [
    "**MacTahoe-dark** (ícones)",
    "Ícones estilo macOS Tahoe"
   ],
   [
    "**Template do Noctalia** + `mactahoe-recolor.py`",
    "Sempre que o esquema muda, pinta as pastas com o tom principal do Noctalia"
   ],
   [
    "**dolphinrc / dolphinui.rc**",
    "Sem menu, toolbar mínima (◀ ▶ · vista · caminho · pesquisa · terminal · menu), slider de zoom, ícones a 64 px"
   ],
   [
    "**Ícones de pastas** (`config/folder-icons.tsv`)",
    "Ícones personalizados por pasta (ex.: `Vault → folder-sign`)"
   ],
   [
    "**Regras do Hyprland** (`hypr/dolphin.lua`)",
    "Janela opaca (o vidro vem do Darkly) e diálogos a flutuar"
   ]
  ],
  "what": "O que acontece por baixo?",
  "happen": [
   "A translucidez é desenhada pelo **Darkly**, widget a widget. O Hyprland mantém a janela em `opacity 1.0` e só faz blur onde o Darkly deixa passar.",
   "O Noctalia gera o `palette.json` a partir do esquema M3 a cada mudança de wallpaper/esquema e corre o `post_hook`.",
   "O hook reescreve os 18 SVG de pastas em `places/scalable` a partir dos originais azuis (`#006efd`) e limpa a cache de ícones do KDE."
  ],
  "pipe": "O matiz vem de `primary.light`, a saturação da mais viva das duas cores principais (com teto em `MAX_SAT`) e a luminosidade é fixa (`LIGHTNESS`). A pasta mantém o matiz do wallpaper sem ficar néon nem desbotada.",
  "req_h": "Requisitos",
  "req": [
   "Arch / CachyOS (usa `paru` ou `yay`)",
   "Hyprland (config em Lua) com blur ligado",
   "Noctalia Shell com os templates `qt` e `kcolorscheme` ativos",
   "`qt6ct` como platform theme (`QT_QPA_PLATFORMTHEME=qt6ct`)",
   "`fish`, `git`, `python3`, `kwriteconfig6`"
  ],
  "fast": "Caminho rápido",
  "user": "mastermaiolo",
  "inst_h": "O que o instalador faz",
  "inst": [
   "instala `darkly`, `inter-font`, `git` e `python` (salta com `--no-deps`);",
   "clona o [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) e instala-o em `~/.local/share/icons`;",
   "copia o template e o script de recoloração para `~/.config/noctalia/` e regista o template no `config.toml`;",
   "aplica `darklyrc`, `qt6ct` (Darkly + MacTahoe-dark), `dolphinrc`, a toolbar e os ícones das pastas."
  ],
  "backup": "Antes de mexer num ficheiro faz sempre uma cópia (`*.bak-AAAAMMDD-HHMMSS`).",
  "manual_h": "Passos manuais",
  "manual": [
   "copiar as regras de [`hypr/dolphin.lua`](hypr/dolphin.lua) para a tua config do Hyprland;",
   "usar `scale >= 1` no monitor (ver *08 / Problemas conhecidos*);",
   "no qt6ct, escolher a fonte **Inter 10**;",
   "fechar e voltar a abrir o Dolphin."
  ],
  "now": "Para aplicar a recoloração na hora:",
  "c_noct": "cor do Noctalia",
  "c_fixed": "cor fixa",
  "fc": "**Cor das pastas:** no topo de `~/.config/noctalia/scripts/mactahoe-recolor.py`.",
  "py_l": "mais baixo = pasta mais escura (Finder ≈ 0.50)",
  "py_s": "0.3 = tonal discreto · 0.8 = vivo",
  "gl": "**Vidro:** em `~/.config/darklyrc`.",
  "gth": [
   "Chave",
   "Valor",
   "Efeito"
  ],
  "glass": [
   [
    "DolphinSidebarOpacity",
    "55",
    "barra lateral (40 = mais vidro, 70 = mais sólido)"
   ],
   [
    "ToolBarOpacity",
    "55",
    "barra de ferramentas"
   ],
   [
    "DolphinViewOpacity",
    "80",
    "área das pastas (subir para 85–90 com wallpapers claros)"
   ]
  ],
  "tb_h": "Bloco do template no Noctalia",
  "tb": "Acrescentado ao `~/.config/noctalia/config.toml` pelo `install.fish` (ou à mão a partir de `noctalia/config.snippet.toml`):",
  "art": "ilustrações do README",
  "long": "Notas detalhadas",
  "fail": [
   "**Blur cortado no fundo ou à direita da janela:** acontece com `scale` do monitor abaixo de 1 (ex.: `0.9375`). O Hyprland recorta o blur em `largura×scale` / `altura×scale`. Solução: `scale = \"1\"`.",
   "**Barras de capacidade nos dispositivos** da barra lateral: o Dolphin não tem opção para as esconder.",
   "**\"16 folders\" em inglês** na barra de estado: são frases que ainda não estão traduzidas no próprio Dolphin.",
   "**As pastas não mudam de cor:** o `post_hook` não correu ou falta o `python3` — corre o `mactahoe-recolor.py` à mão.",
   "**Instalar o MacTahoe outra vez** pode mostrar avisos `cannot remove`: não têm importância."
  ],
  "un_h": "Apêndice — desinstalar",
  "then": "Depois:",
  "un": [
   "remove o bloco `[theme.templates.user.mactahoe]` do `config.toml` do Noctalia;",
   "repõe os `*.bak-*` que quiseres."
  ],
  "prov": [
   "[MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme), de vinceliuice — descarregado durante a instalação, não vem incluído aqui.",
   "[Darkly](https://github.com/Bali10050/Darkly) — estilo Qt.",
   "[Noctalia](https://noctalia.dev) — shell e motor de templates."
  ],
  "lic": [
   "Scripts e configs deste repositório: [MIT](LICENSE).",
   "MacTahoe-icon-theme: GPL-3.0 (licença do projeto original)."
  ]
 },
 "pt-br": {
  "alt_hero": "Dolphin estilo Finder para Hyprland + Noctalia",
  "lead": "Dolphin com cara de **Finder do macOS** no **Hyprland + Noctalia**: barra lateral de vidro, ícones **MacTahoe** e pastas que **mudam de cor com o papel de parede**, seguindo a paleta tonal (Material You) do Noctalia.",
  "alt_shot": "Dolphin com barra lateral de vidro, ícones MacTahoe e pastas tonais rosadas",
  "h": [
   "VISÃO GERAL",
   "RECURSOS",
   "PIPELINE TONAL",
   "INSTALAÇÃO",
   "SUPERFÍCIE DE CONTROLE",
   "CONFIGURAÇÃO",
   "ARQUITETURA",
   "PROBLEMAS CONHECIDOS",
   "PROCEDÊNCIA",
   "LICENÇA"
  ],
  "th": [
   "Peça",
   "O que faz"
  ],
  "pieces": [
   [
    "**Darkly** (estilo Qt6)",
    "Cantos arredondados; barra lateral e barra de ferramentas translúcidas, vidro sutil na área das pastas; sem linha de foco nem separadores"
   ],
   [
    "**MacTahoe-dark** (ícones)",
    "Ícones estilo macOS Tahoe"
   ],
   [
    "**Template do Noctalia** + `mactahoe-recolor.py`",
    "Sempre que o esquema muda, pinta as pastas com o tom principal do Noctalia"
   ],
   [
    "**dolphinrc / dolphinui.rc**",
    "Sem barra de menus, barra de ferramentas mínima (◀ ▶ · visualização · caminho · pesquisa · terminal · menu), controle de zoom, ícones de 64 px"
   ],
   [
    "**Ícones de pastas** (`config/folder-icons.tsv`)",
    "Ícones personalizados por pasta (ex.: `Vault → folder-sign`)"
   ],
   [
    "**Regras do Hyprland** (`hypr/dolphin.lua`)",
    "Janela opaca (o vidro vem do Darkly) e diálogos flutuantes"
   ]
  ],
  "what": "O que acontece por trás?",
  "happen": [
   "A translucidez é desenhada pelo **Darkly**, widget por widget. O Hyprland mantém a janela em `opacity 1.0` e só aplica blur onde o Darkly deixa passar.",
   "O Noctalia gera o `palette.json` a partir do esquema M3 a cada troca de papel de parede/esquema e executa o `post_hook`.",
   "O hook reescreve os 18 SVGs de pastas em `places/scalable` a partir dos originais azuis (`#006efd`) e limpa o cache de ícones do KDE."
  ],
  "pipe": "O matiz vem de `primary.light`, a saturação da mais viva das duas cores primárias (limitada por `MAX_SAT`) e a luminosidade é fixa (`LIGHTNESS`). A pasta mantém o matiz do papel de parede sem ficar neon nem desbotada.",
  "req_h": "Requisitos",
  "req": [
   "Arch / CachyOS (usa `paru` ou `yay`)",
   "Hyprland (config em Lua) com blur ativado",
   "Noctalia Shell com os templates `qt` e `kcolorscheme` ativos",
   "`qt6ct` como platform theme (`QT_QPA_PLATFORMTHEME=qt6ct`)",
   "`fish`, `git`, `python3`, `kwriteconfig6`"
  ],
  "fast": "Caminho rápido",
  "user": "mastermaiolo",
  "inst_h": "O que o instalador faz",
  "inst": [
   "instala `darkly`, `inter-font`, `git` e `python` (pule com `--no-deps`);",
   "clona o [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) e o instala em `~/.local/share/icons`;",
   "copia o template e o script de recoloração para `~/.config/noctalia/` e registra o template no `config.toml`;",
   "aplica `darklyrc`, `qt6ct` (Darkly + MacTahoe-dark), `dolphinrc`, a barra de ferramentas e os ícones das pastas."
  ],
  "backup": "Antes de alterar qualquer arquivo, ele faz um backup (`*.bak-AAAAMMDD-HHMMSS`).",
  "manual_h": "Passos manuais",
  "manual": [
   "copiar as regras de [`hypr/dolphin.lua`](hypr/dolphin.lua) para a sua config do Hyprland;",
   "usar `scale >= 1` no monitor (veja *08 / Problemas conhecidos*);",
   "no qt6ct, escolher a fonte **Inter 10**;",
   "fechar e abrir o Dolphin de novo."
  ],
  "now": "Para aplicar a recoloração na hora:",
  "c_noct": "cor do Noctalia",
  "c_fixed": "cor fixa",
  "fc": "**Cor das pastas:** no topo de `~/.config/noctalia/scripts/mactahoe-recolor.py`.",
  "py_l": "mais baixo = pasta mais escura (Finder ≈ 0.50)",
  "py_s": "0.3 = tonal discreto · 0.8 = vivo",
  "gl": "**Vidro:** em `~/.config/darklyrc`.",
  "gth": [
   "Chave",
   "Valor",
   "Efeito"
  ],
  "glass": [
   [
    "DolphinSidebarOpacity",
    "55",
    "barra lateral (40 = mais vidro, 70 = mais sólido)"
   ],
   [
    "ToolBarOpacity",
    "55",
    "barra de ferramentas"
   ],
   [
    "DolphinViewOpacity",
    "80",
    "área das pastas (aumente para 85–90 com papéis de parede claros)"
   ]
  ],
  "tb_h": "Bloco do template no Noctalia",
  "tb": "Adicionado ao `~/.config/noctalia/config.toml` pelo `install.fish` (ou manualmente a partir de `noctalia/config.snippet.toml`):",
  "art": "ilustrações do README",
  "long": "Notas detalhadas",
  "fail": [
   "**Blur cortado embaixo ou à direita da janela:** acontece com `scale` do monitor abaixo de 1 (ex.: `0.9375`). O Hyprland recorta o blur em `largura×scale` / `altura×scale`. Solução: `scale = \"1\"`.",
   "**Barras de capacidade nos dispositivos** da barra lateral: o Dolphin não tem opção para escondê-las.",
   "**\"16 folders\" em inglês** na barra de status: são textos que ainda não foram traduzidos no próprio Dolphin.",
   "**As pastas não mudam de cor:** o `post_hook` não rodou ou falta o `python3` — rode o `mactahoe-recolor.py` manualmente.",
   "**Reinstalar o MacTahoe** pode mostrar avisos `cannot remove`: são inofensivos."
  ],
  "un_h": "Apêndice — desinstalar",
  "then": "Depois:",
  "un": [
   "remova o bloco `[theme.templates.user.mactahoe]` do `config.toml` do Noctalia;",
   "restaure os `*.bak-*` que quiser."
  ],
  "prov": [
   "[MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme), de vinceliuice — baixado durante a instalação, não vem incluído aqui.",
   "[Darkly](https://github.com/Bali10050/Darkly) — estilo Qt.",
   "[Noctalia](https://noctalia.dev) — shell e motor de templates."
  ],
  "lic": [
   "Scripts e configs deste repositório: [MIT](LICENSE).",
   "MacTahoe-icon-theme: GPL-3.0 (licença do projeto original)."
  ]
 },
 "es-es": {
  "alt_hero": "Dolphin estilo Finder para Hyprland + Noctalia",
  "lead": "Dolphin con aspecto de **Finder de macOS** en **Hyprland + Noctalia**: barra lateral de cristal, iconos **MacTahoe** y carpetas que **cambian de color con el fondo de pantalla**, siguiendo la paleta tonal (Material You) de Noctalia.",
  "alt_shot": "Dolphin con barra lateral de cristal, iconos MacTahoe y carpetas tonales rosadas",
  "h": [
   "DE UN VISTAZO",
   "CAPACIDADES",
   "CANAL TONAL",
   "INSTALACIÓN",
   "SUPERFICIE DE CONTROL",
   "CONFIGURACIÓN",
   "ARQUITECTURA",
   "PROBLEMAS CONOCIDOS",
   "PROCEDENCIA",
   "LICENCIA"
  ],
  "th": [
   "Pieza",
   "Qué hace"
  ],
  "pieces": [
   [
    "**Darkly** (estilo Qt6)",
    "Esquinas redondeadas; barra lateral y barra de herramientas translúcidas, cristal sutil en el área de archivos; sin línea de foco ni separadores"
   ],
   [
    "**MacTahoe-dark** (iconos)",
    "Iconos al estilo macOS Tahoe"
   ],
   [
    "**Plantilla de Noctalia** + `mactahoe-recolor.py`",
    "Cada vez que cambia el esquema, pinta las carpetas con el tono principal de Noctalia"
   ],
   [
    "**dolphinrc / dolphinui.rc**",
    "Sin menú, barra de herramientas mínima (◀ ▶ · vista · ruta · búsqueda · terminal · menú), control de zoom, iconos de 64 px"
   ],
   [
    "**Iconos de carpetas** (`config/folder-icons.tsv`)",
    "Iconos personalizados por carpeta (p. ej. `Vault → folder-sign`)"
   ],
   [
    "**Reglas de Hyprland** (`hypr/dolphin.lua`)",
    "Ventana opaca (el cristal lo pone Darkly) y diálogos flotantes"
   ]
  ],
  "what": "¿Qué ocurre por debajo?",
  "happen": [
   "La translucidez la dibuja **Darkly**, widget a widget. Hyprland mantiene la ventana en `opacity 1.0` y solo aplica desenfoque donde Darkly deja ver.",
   "Noctalia genera `palette.json` a partir de su esquema M3 en cada cambio de fondo/esquema y ejecuta el `post_hook`.",
   "El hook reescribe los 18 SVG de carpetas en `places/scalable` a partir de los originales azules (`#006efd`) y vacía la caché de iconos de KDE."
  ],
  "pipe": "El matiz sale de `primary.light`, la saturación del más vivo de los dos primarios (con tope en `MAX_SAT`) y la luminosidad es fija (`LIGHTNESS`). La carpeta conserva el matiz del fondo sin volverse neón ni desvaída.",
  "req_h": "Requisitos",
  "req": [
   "Arch / CachyOS (usa `paru` o `yay`)",
   "Hyprland (configuración en Lua) con desenfoque activado",
   "Noctalia Shell con las plantillas `qt` y `kcolorscheme` activas",
   "`qt6ct` como platform theme (`QT_QPA_PLATFORMTHEME=qt6ct`)",
   "`fish`, `git`, `python3`, `kwriteconfig6`"
  ],
  "fast": "Vía rápida",
  "user": "mastermaiolo",
  "inst_h": "Qué hace el instalador",
  "inst": [
   "instala `darkly`, `inter-font`, `git` y `python` (se omite con `--no-deps`);",
   "clona [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) y lo instala en `~/.local/share/icons`;",
   "copia la plantilla y el script de recoloreado a `~/.config/noctalia/` y registra la plantilla en `config.toml`;",
   "aplica `darklyrc`, `qt6ct` (Darkly + MacTahoe-dark), `dolphinrc`, la barra de herramientas y los iconos de carpetas."
  ],
  "backup": "Antes de tocar un fichero siempre hace una copia (`*.bak-AAAAMMDD-HHMMSS`).",
  "manual_h": "Pasos manuales",
  "manual": [
   "copia las reglas de [`hypr/dolphin.lua`](hypr/dolphin.lua) a tu configuración de Hyprland;",
   "usa `scale >= 1` en el monitor (ver *08 / Problemas conocidos*);",
   "en qt6ct, elige la fuente **Inter 10**;",
   "cierra y vuelve a abrir Dolphin."
  ],
  "now": "Para aplicar el recoloreado al momento:",
  "c_noct": "color de Noctalia",
  "c_fixed": "color fijo",
  "fc": "**Color de las carpetas:** al principio de `~/.config/noctalia/scripts/mactahoe-recolor.py`.",
  "py_l": "más bajo = carpeta más oscura (Finder ≈ 0.50)",
  "py_s": "0.3 = tonal discreto · 0.8 = vivo",
  "gl": "**Cristal:** en `~/.config/darklyrc`.",
  "gth": [
   "Clave",
   "Valor",
   "Efecto"
  ],
  "glass": [
   [
    "DolphinSidebarOpacity",
    "55",
    "barra lateral (40 = más cristal, 70 = más sólida)"
   ],
   [
    "ToolBarOpacity",
    "55",
    "barra de herramientas"
   ],
   [
    "DolphinViewOpacity",
    "80",
    "área de archivos (súbelo a 85–90 con fondos claros)"
   ]
  ],
  "tb_h": "Bloque de plantilla de Noctalia",
  "tb": "Añadido a `~/.config/noctalia/config.toml` por `install.fish` (o a mano desde `noctalia/config.snippet.toml`):",
  "art": "ilustraciones del README",
  "long": "Notas detalladas",
  "fail": [
   "**Desenfoque cortado abajo o a la derecha de la ventana:** ocurre con un `scale` del monitor inferior a 1 (p. ej. `0.9375`). Hyprland recorta el desenfoque en `ancho×scale` / `alto×scale`. Solución: `scale = \"1\"`.",
   "**Barras de capacidad en los dispositivos** de la barra lateral: Dolphin no tiene opción para ocultarlas.",
   "**\"16 folders\" en inglés** en la barra de estado: son textos que aún no están traducidos en el propio Dolphin.",
   "**Las carpetas no cambian de color:** el `post_hook` no se ejecutó o falta `python3` — ejecuta `mactahoe-recolor.py` a mano.",
   "**Reinstalar MacTahoe** puede mostrar avisos `cannot remove`: son inofensivos."
  ],
  "un_h": "Apéndice — desinstalar",
  "then": "Después:",
  "un": [
   "elimina el bloque `[theme.templates.user.mactahoe]` del `config.toml` de Noctalia;",
   "restaura los `*.bak-*` que quieras."
  ],
  "prov": [
   "[MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme), de vinceliuice — se descarga durante la instalación, no se incluye aquí.",
   "[Darkly](https://github.com/Bali10050/Darkly) — estilo Qt.",
   "[Noctalia](https://noctalia.dev) — shell y motor de plantillas."
  ],
  "lic": [
   "Scripts y configuraciones de este repositorio: [MIT](LICENSE).",
   "MacTahoe-icon-theme: GPL-3.0 (licencia del proyecto original)."
  ]
 },
 "zh-cn": {
  "alt_hero": "面向 Hyprland + Noctalia 的 Finder 风格 Dolphin",
  "lead": "在 **Hyprland + Noctalia** 上把 Dolphin 打造成 **macOS Finder** 风格:玻璃质感侧边栏、**MacTahoe** 图标,以及**随壁纸变色**的文件夹,跟随 Noctalia 的色调(Material You)调色板。",
  "alt_shot": "带玻璃侧边栏、MacTahoe 图标和玫瑰色调文件夹的 Dolphin",
  "h": [
   "概览",
   "功能",
   "色调管线",
   "安装",
   "控制面板",
   "配置",
   "架构",
   "故障排查",
   "来源",
   "许可证"
  ],
  "th": [
   "组件",
   "作用"
  ],
  "pieces": [
   [
    "**Darkly**(Qt6 样式)",
    "圆角;半透明侧边栏和工具栏,文件区域带轻微玻璃效果;无焦点线、无分隔线"
   ],
   [
    "**MacTahoe-dark**(图标)",
    "macOS Tahoe 风格图标"
   ],
   [
    "**Noctalia 模板** + `mactahoe-recolor.py`",
    "每当配色方案变化,用 Noctalia 的主色调重新着色文件夹"
   ],
   [
    "**dolphinrc / dolphinui.rc**",
    "无菜单栏,精简工具栏(◀ ▶ · 视图 · 路径 · 搜索 · 终端 · 菜单),缩放滑块,64 px 图标"
   ],
   [
    "**文件夹图标**(`config/folder-icons.tsv`)",
    "按文件夹自定义图标(例如 `Vault → folder-sign`)"
   ],
   [
    "**Hyprland 规则**(`hypr/dolphin.lua`)",
    "窗口保持不透明(玻璃效果来自 Darkly),对话框浮动"
   ]
  ],
  "what": "底层发生了什么?",
  "happen": [
   "半透明效果由 **Darkly** 按控件绘制。Hyprland 让窗口保持 `opacity 1.0`,只对 Darkly 留出的透明区域做模糊。",
   "每次壁纸/配色变化时,Noctalia 根据 M3 配色生成 `palette.json`,然后运行 `post_hook`。",
   "该钩子以原始蓝色 SVG(`#006efd`)为基础,重写 `places/scalable` 中的 18 个文件夹 SVG,并清空 KDE 图标缓存。"
  ],
  "pipe": "色相取自 `primary.light`,饱和度取两种主色中更鲜艳的一个(上限为 `MAX_SAT`),亮度固定(`LIGHTNESS`)。文件夹保留壁纸的色相,既不会过于刺眼,也不会发灰。",
  "req_h": "环境要求",
  "req": [
   "Arch / CachyOS(使用 `paru` 或 `yay`)",
   "Hyprland(Lua 配置)并启用模糊",
   "Noctalia Shell,启用 `qt` 和 `kcolorscheme` 模板",
   "`qt6ct` 作为 platform theme(`QT_QPA_PLATFORMTHEME=qt6ct`)",
   "`fish`、`git`、`python3`、`kwriteconfig6`"
  ],
  "fast": "快速安装",
  "user": "mastermaiolo",
  "inst_h": "安装脚本做了什么",
  "inst": [
   "安装 `darkly`、`inter-font`、`git` 和 `python`(用 `--no-deps` 跳过);",
   "克隆 [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) 并安装到 `~/.local/share/icons`;",
   "把模板和重新着色脚本复制到 `~/.config/noctalia/`,并在 `config.toml` 中注册模板;",
   "应用 `darklyrc`、`qt6ct`(Darkly + MacTahoe-dark)、`dolphinrc`、工具栏和文件夹图标。"
  ],
  "backup": "修改任何文件之前都会先备份(`*.bak-YYYYMMDD-HHMMSS`)。",
  "manual_h": "手动步骤",
  "manual": [
   "把 [`hypr/dolphin.lua`](hypr/dolphin.lua) 中的规则复制到你的 Hyprland 配置;",
   "显示器使用 `scale >= 1`(见 *08 / 故障排查*);",
   "在 qt6ct 中选择 **Inter 10** 字体;",
   "关闭并重新打开 Dolphin。"
  ],
  "now": "立即应用重新着色:",
  "c_noct": "Noctalia 颜色",
  "c_fixed": "固定颜色",
  "fc": "**文件夹颜色:** 位于 `~/.config/noctalia/scripts/mactahoe-recolor.py` 顶部。",
  "py_l": "越低 = 文件夹越暗(Finder ≈ 0.50)",
  "py_s": "0.3 = 低调色调 · 0.8 = 鲜艳",
  "gl": "**玻璃效果:** 位于 `~/.config/darklyrc`。",
  "gth": [
   "键",
   "值",
   "效果"
  ],
  "glass": [
   [
    "DolphinSidebarOpacity",
    "55",
    "侧边栏(40 = 更通透,70 = 更实)"
   ],
   [
    "ToolBarOpacity",
    "55",
    "工具栏"
   ],
   [
    "DolphinViewOpacity",
    "80",
    "文件区域(浅色壁纸可调到 85–90)"
   ]
  ],
  "tb_h": "Noctalia 模板配置块",
  "tb": "由 `install.fish` 添加到 `~/.config/noctalia/config.toml`(或从 `noctalia/config.snippet.toml` 手动添加):",
  "art": "README 插图",
  "long": "详细说明",
  "fail": [
   "**窗口底部或右侧的模糊被截断:** 显示器 `scale` 小于 1(例如 `0.9375`)时出现。Hyprland 会在 `宽×scale` / `高×scale` 处截断模糊。解决:`scale = \"1\"`。",
   "**侧边栏设备下的容量条:** Dolphin 没有隐藏它们的选项。",
   "**状态栏中的英文 \"16 folders\":** 这些字符串在 Dolphin 本身中尚未翻译。",
   "**文件夹颜色不变:** `post_hook` 没有运行或缺少 `python3` — 手动运行 `mactahoe-recolor.py`。",
   "**重新安装 MacTahoe** 可能出现 `cannot remove` 警告:无害。"
  ],
  "un_h": "附录 — 卸载",
  "then": "然后:",
  "un": [
   "从 Noctalia 的 `config.toml` 中删除 `[theme.templates.user.mactahoe]` 配置块;",
   "按需恢复 `*.bak-*` 备份文件。"
  ],
  "prov": [
   "[MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme),作者 vinceliuice — 安装时下载,本仓库不包含。",
   "[Darkly](https://github.com/Bali10050/Darkly) — Qt 样式。",
   "[Noctalia](https://noctalia.dev) — Shell 与模板引擎。"
  ],
  "lic": [
   "本仓库的脚本与配置:[MIT](LICENSE)。",
   "MacTahoe-icon-theme:GPL-3.0(上游许可证)。"
  ]
 }
}
import os
json.dump(L, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lang.json"), "w"), ensure_ascii=False)
