# dolphin-finder-noctalia

Dolphin com cara de **Finder do macOS** em **Hyprland + Noctalia**: barra lateral de vidro, ícones **MacTahoe** e pastas que **mudam de cor com o wallpaper**, seguindo a paleta tonal (Material You) do Noctalia.

![screenshot](screenshots/dolphin.png)

## O que inclui

| Peça | O que faz |
|---|---|
| **Darkly** (estilo Qt6) | Cantos arredondados; barra lateral e toolbar translúcidas, área das pastas com vidro subtil; sem linha de foco nem separadores |
| **MacTahoe-dark** (ícones) | Ícones estilo macOS Tahoe |
| **Template do Noctalia** + `mactahoe-recolor.py` | Sempre que o esquema muda, pinta as pastas com o tom principal do Noctalia |
| **dolphinrc / dolphinui.rc** | Sem menu, toolbar mínima (◀ ▶ · vista · caminho · pesquisa · terminal · menu), slider de zoom, ícones a 64 px |
| **Ícones de pastas** (`config/folder-icons.tsv`) | Ícones personalizados por pasta (ex.: `Vault → folder-sign`) |
| **Regras do Hyprland** (`hypr/dolphin.lua`) | Janela opaca (o vidro vem do Darkly) e diálogos a flutuar |

## Requisitos

- Arch / CachyOS (usa `paru` ou `yay`)
- Hyprland (config em Lua) com blur ligado
- Noctalia Shell com os templates `qt` e `kcolorscheme` ativos
- `qt6ct` como platform theme (`QT_QPA_PLATFORMTHEME=qt6ct`)
- `fish`, `git`, `python3`, `kwriteconfig6`

## Instalação

```fish
git clone https://github.com/<o-teu-utilizador>/dolphin-finder-noctalia.git
cd dolphin-finder-noctalia
./install.fish
```

O script:

1. instala `darkly`, `inter-font`, `git` e `python` (salta com `--no-deps`);
2. clona o [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) e instala-o em `~/.local/share/icons`;
3. copia o template e o script de recoloração para `~/.config/noctalia/` e regista o template no `config.toml`;
4. aplica `darklyrc`, `qt6ct` (Darkly + MacTahoe-dark), `dolphinrc`, a toolbar e os ícones das pastas.

Antes de mexer num ficheiro faz sempre uma cópia (`*.bak-AAAAMMDD-HHMMSS`).

**Passos manuais:**

- copiar as regras de [`hypr/dolphin.lua`](hypr/dolphin.lua) para a tua config do Hyprland;
- usar `scale >= 1` no monitor (ver *Problemas conhecidos*);
- no qt6ct, escolher a fonte **Inter 10**;
- fechar e voltar a abrir o Dolphin.

## Afinar

**Cor das pastas:** no topo de `~/.config/noctalia/scripts/mactahoe-recolor.py`.

```python
LIGHTNESS = 0.58   # mais baixo = pasta mais escura (Finder ≈ 0.50)
MAX_SAT   = 0.60   # 0.3 = tonal discreto · 0.8 = vivo
```

Para aplicar na hora:

```fish
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py            # cor do Noctalia
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py '#1a8fe8'  # cor fixa
```

**Vidro:** em `~/.config/darklyrc`.

| Chave | Valor | Efeito |
|---|---|---|
| `DolphinSidebarOpacity` | 55 | barra lateral (40 = mais vidro, 70 = mais sólido) |
| `ToolBarOpacity` | 55 | barra de ferramentas |
| `DolphinViewOpacity` | 80 | área das pastas (subir para 85–90 com wallpapers claros) |

## Problemas conhecidos

- **Blur cortado no fundo ou à direita da janela:** acontece com `scale` do monitor abaixo de 1 (ex.: `0.9375`). O Hyprland recorta o blur em `largura×scale` / `altura×scale`. Solução: `scale = "1"`.
- **Barras de capacidade nos dispositivos** da barra lateral: o Dolphin não tem opção para as esconder.
- **"16 folders" em inglês** na barra de estado: são frases que ainda não estão traduzidas no próprio Dolphin.
- **Instalar o MacTahoe outra vez** pode mostrar avisos `cannot remove`: não têm importância.

## Desinstalar

```fish
rm -rf ~/.local/share/icons/MacTahoe{,-dark,-light} ~/.local/share/mactahoe-noctalia
rm ~/.config/noctalia/scripts/mactahoe-recolor.py
rm -r ~/.config/noctalia/templates/mactahoe
```

Depois:

- remove o bloco `[theme.templates.user.mactahoe]` do `config.toml` do Noctalia;
- repõe os `*.bak-*` que quiseres.

## Créditos e licenças

- Scripts e configs deste repositório: [MIT](LICENSE).
- [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme), de vinceliuice: GPL-3.0. É descarregado durante a instalação e não vem incluído aqui.
- [Darkly](https://github.com/Bali10050/Darkly): estilo Qt.
- [Noctalia](https://noctalia.dev): shell e motor de templates.
