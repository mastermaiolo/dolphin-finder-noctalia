<p align="center">
  <img src="assets/readme/hero.svg" width="100%" alt="dolphin-finder-noctalia — Dolphin estilo Finder para Hyprland + Noctalia">
</p>

<p align="center"><sub><strong>KDE DOLPHIN · DARKLY · MACTAHOE · HYPRLAND · NOCTALIA</strong></sub></p>

<p align="center">
  <a href="README.md">🇬🇧 English (UK)</a>
  · 🇧🇷 <strong>Português (BR)</strong>
  · <a href="README.pt-pt.md">🇵🇹 Português (PT)</a>
  · <a href="README.es-es.md">🇪🇸 Español (ES)</a>
  · <a href="README.zh-cn.md">🇨🇳 简体中文</a>
</p>

> Dolphin com cara de **Finder do macOS** no **Hyprland + Noctalia**: barra lateral de vidro, ícones **MacTahoe** e pastas que **mudam de cor com o papel de parede**, seguindo a paleta tonal (Material You) do Noctalia.

<p align="center">
  <img src="screenshots/dolphin.png" width="100%" alt="Dolphin com barra lateral de vidro, ícones MacTahoe e pastas tonais rosadas">
</p>

---

## 01 / VISÃO GERAL

<p align="center">
  <img src="assets/readme/at-a-glance.svg" width="100%" alt="Darkly · MacTahoe-dark · Noctalia M3 · Hyprland">
</p>

## 02 / RECURSOS

<p align="center">
  <img src="assets/readme/capabilities.svg" width="100%" alt="RECURSOS">
</p>

| Peça | O que faz |
|---|---|
| **Darkly** (estilo Qt6) | Cantos arredondados; barra lateral e barra de ferramentas translúcidas, vidro sutil na área das pastas; sem linha de foco nem separadores |
| **MacTahoe-dark** (ícones) | Ícones estilo macOS Tahoe |
| **Template do Noctalia** + `mactahoe-recolor.py` | Sempre que o esquema muda, pinta as pastas com o tom principal do Noctalia |
| **dolphinrc / dolphinui.rc** | Sem barra de menus, barra de ferramentas mínima (◀ ▶ · visualização · caminho · pesquisa · terminal · menu), controle de zoom, ícones de 64 px |
| **Ícones de pastas** (`config/folder-icons.tsv`) | Ícones personalizados por pasta (ex.: `Vault → folder-sign`) |
| **Regras do Hyprland** (`hypr/dolphin.lua`) | Janela opaca (o vidro vem do Darkly) e diálogos flutuantes |

### O que acontece por trás?

- A translucidez é desenhada pelo **Darkly**, widget por widget. O Hyprland mantém a janela em `opacity 1.0` e só aplica blur onde o Darkly deixa passar.
- O Noctalia gera o `palette.json` a partir do esquema M3 a cada troca de papel de parede/esquema e executa o `post_hook`.
- O hook reescreve os 18 SVGs de pastas em `places/scalable` a partir dos originais azuis (`#006efd`) e limpa o cache de ícones do KDE.

## 03 / PIPELINE TONAL

<p align="center">
  <img src="assets/readme/tonal-pipeline.svg" width="100%" alt="wallpaper → M3 → palette.json → mactahoe-recolor.py → icons">
</p>

O matiz vem de `primary.light`, a saturação da mais viva das duas cores primárias (limitada por `MAX_SAT`) e a luminosidade é fixa (`LIGHTNESS`). A pasta mantém o matiz do papel de parede sem ficar neon nem desbotada.

## 04 / INSTALAÇÃO

### Requisitos

- Arch / CachyOS (usa `paru` ou `yay`)
- Hyprland (config em Lua) com blur ativado
- Noctalia Shell com os templates `qt` e `kcolorscheme` ativos
- `qt6ct` como platform theme (`QT_QPA_PLATFORMTHEME=qt6ct`)
- `fish`, `git`, `python3`, `kwriteconfig6`

### Caminho rápido

```fish
git clone https://github.com/mastermaiolo/dolphin-finder-noctalia.git
cd dolphin-finder-noctalia
./install.fish
```

<details>
<summary><strong>O que o instalador faz</strong></summary>

1. instala `darkly`, `inter-font`, `git` e `python` (pule com `--no-deps`);
2. clona o [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) e o instala em `~/.local/share/icons`;
3. copia o template e o script de recoloração para `~/.config/noctalia/` e registra o template no `config.toml`;
4. aplica `darklyrc`, `qt6ct` (Darkly + MacTahoe-dark), `dolphinrc`, a barra de ferramentas e os ícones das pastas.

Antes de alterar qualquer arquivo, ele faz um backup (`*.bak-AAAAMMDD-HHMMSS`).

</details>

### Passos manuais

- copiar as regras de [`hypr/dolphin.lua`](hypr/dolphin.lua) para a sua config do Hyprland;
- usar `scale >= 1` no monitor (veja *08 / Problemas conhecidos*);
- no qt6ct, escolher a fonte **Inter 10**;
- fechar e abrir o Dolphin de novo.

## 05 / SUPERFÍCIE DE CONTROLE

<p align="center">
  <img src="assets/readme/control-surface.svg" width="100%" alt="LIGHTNESS · MAX_SAT · darklyrc">
</p>

Para aplicar a recoloração na hora:

```fish
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py            # cor do Noctalia
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py '#1a8fe8'  # cor fixa
```

## 06 / CONFIGURAÇÃO

**Cor das pastas:** no topo de `~/.config/noctalia/scripts/mactahoe-recolor.py`.

```python
LIGHTNESS = 0.58   # mais baixo = pasta mais escura (Finder ≈ 0.50)
MAX_SAT   = 0.60   # 0.3 = tonal discreto · 0.8 = vivo
```

**Vidro:** em `~/.config/darklyrc`.

| Chave | Valor | Efeito |
|---|---|---|
| `DolphinSidebarOpacity` | 55 | barra lateral (40 = mais vidro, 70 = mais sólido) |
| `ToolBarOpacity` | 55 | barra de ferramentas |
| `DolphinViewOpacity` | 80 | área das pastas (aumente para 85–90 com papéis de parede claros) |

<details>
<summary><strong>Bloco do template no Noctalia</strong></summary>

Adicionado ao `~/.config/noctalia/config.toml` pelo `install.fish` (ou manualmente a partir de `noctalia/config.snippet.toml`):

```toml
[theme.templates.user.mactahoe]
input_path = "$HOME/.config/noctalia/templates/mactahoe/palette.json"
output_path = "$HOME/.local/state/mactahoe-noctalia/palette.json"
post_hook = "python3 $HOME/.config/noctalia/scripts/mactahoe-recolor.py"
```

</details>

## 07 / ARQUITETURA

<p align="center">
  <img src="assets/readme/architecture.svg" width="100%" alt="ARQUITETURA">
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
├── assets/readme/          # ilustrações do README
└── screenshots/
```

## 08 / PROBLEMAS CONHECIDOS

<p align="center">
  <img src="assets/readme/failure-modes.svg" width="100%" alt="PROBLEMAS CONHECIDOS">
</p>

<details>
<summary><strong>Notas detalhadas</strong></summary>

- **Blur cortado embaixo ou à direita da janela:** acontece com `scale` do monitor abaixo de 1 (ex.: `0.9375`). O Hyprland recorta o blur em `largura×scale` / `altura×scale`. Solução: `scale = "1"`.
- **Barras de capacidade nos dispositivos** da barra lateral: o Dolphin não tem opção para escondê-las.
- **"16 folders" em inglês** na barra de status: são textos que ainda não foram traduzidos no próprio Dolphin.
- **As pastas não mudam de cor:** o `post_hook` não rodou ou falta o `python3` — rode o `mactahoe-recolor.py` manualmente.
- **Reinstalar o MacTahoe** pode mostrar avisos `cannot remove`: são inofensivos.

</details>

<details>
<summary><strong>Apêndice — desinstalar</strong></summary>

```fish
rm -rf ~/.local/share/icons/MacTahoe{,-dark,-light} ~/.local/share/mactahoe-noctalia
rm ~/.config/noctalia/scripts/mactahoe-recolor.py
rm -r ~/.config/noctalia/templates/mactahoe
```

Depois:

- remova o bloco `[theme.templates.user.mactahoe]` do `config.toml` do Noctalia;
- restaure os `*.bak-*` que quiser.

</details>

## 09 / PROCEDÊNCIA

<p align="center">
  <img src="assets/readme/provenance.svg" width="100%" alt="MacTahoe · Darkly · Noctalia · MIT">
</p>

- [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme), de vinceliuice — baixado durante a instalação, não vem incluído aqui.
- [Darkly](https://github.com/Bali10050/Darkly) — estilo Qt.
- [Noctalia](https://noctalia.dev) — shell e motor de templates.

## 10 / LICENÇA

- Scripts e configs deste repositório: [MIT](LICENSE).
- MacTahoe-icon-theme: GPL-3.0 (licença do projeto original).

---

<p align="center"><sub>MAIOLO / SYSTEMS LAB · DFN</sub></p>
