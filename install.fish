#!/usr/bin/env fish
# dolphin-finder-noctalia — instala o visual "Finder" no Dolphin (Hyprland + Noctalia)
# Uso: ./install.fish            (instala tudo)
#      ./install.fish --no-deps  (não instala pacotes)

set -l repo (status dirname)
set -g stamp (date +%Y%m%d-%H%M%S)
set -l cfg $HOME/.config

function info; set_color brcyan; echo "→ $argv"; set_color normal; end
function warn; set_color yellow; echo "! $argv"; set_color normal; end
function backup --argument-names f
    test -e $f; and cp $f $f.bak-$stamp; and info "backup: $f.bak-$stamp"
end

# 1. Dependências ---------------------------------------------------------
if not contains -- --no-deps $argv
    set -l helper (command -v paru; or command -v yay)
    if test -n "$helper"
        info "A instalar dependências com $helper"
        $helper -S --needed darkly inter-font git python
    else
        warn "Sem paru/yay: instala à mão darkly, inter-font, git, python"
    end
end

# 2. MacTahoe icon theme --------------------------------------------------
set -l mt (mktemp -d)/MacTahoe-icon-theme
begin
    info "A clonar MacTahoe-icon-theme"
    git clone --depth 1 https://github.com/vinceliuice/MacTahoe-icon-theme.git $mt
    or begin; warn "git clone falhou"; exit 1; end
end
info "A instalar MacTahoe em ~/.local/share/icons"
$mt/install.sh -d $HOME/.local/share/icons

# SVG originais (azul #006efd) — base para a recoloração
set -l orig $HOME/.local/share/mactahoe-noctalia/orig
mkdir -p $orig
cp $mt/colors/color-blue/*.svg $orig/

# 3. Noctalia: template + script de recoloração ---------------------------
mkdir -p $cfg/noctalia/templates/mactahoe $cfg/noctalia/scripts
cp $repo/noctalia/templates/mactahoe/palette.json $cfg/noctalia/templates/mactahoe/
cp $repo/noctalia/scripts/mactahoe-recolor.py $cfg/noctalia/scripts/
chmod +x $cfg/noctalia/scripts/mactahoe-recolor.py

set -l ntoml $cfg/noctalia/config.toml
if test -f $ntoml; and not grep -q 'theme.templates.user.mactahoe' $ntoml
    backup $ntoml
    printf '\n    [theme.templates.user.mactahoe]\n    input_path = "%s"\n    output_path = "%s"\n    post_hook = "python3 %s"\n' \
        $cfg/noctalia/templates/mactahoe/palette.json \
        $HOME/.local/state/mactahoe-noctalia/palette.json \
        $cfg/noctalia/scripts/mactahoe-recolor.py >> $ntoml
    info "Template 'mactahoe' acrescentado ao Noctalia"
else if not test -f $ntoml
    warn "Sem $ntoml — acrescenta à mão o conteúdo de noctalia/config.snippet.toml"
end

# 4. Darkly ---------------------------------------------------------------
backup $cfg/darklyrc
cp $repo/config/darklyrc $cfg/darklyrc

# 5. qt6ct: estilo Darkly + ícones MacTahoe -------------------------------
set -l qt $cfg/qt6ct/qt6ct.conf
if test -f $qt
    backup $qt
    sed -i -e 's/^style=.*/style=Darkly/' -e 's/^icon_theme=.*/icon_theme=MacTahoe-dark/' $qt
    grep -q '^style=' $qt; or sed -i '/^\[Appearance\]/a style=Darkly' $qt
    grep -q '^icon_theme=' $qt; or sed -i '/^\[Appearance\]/a icon_theme=MacTahoe-dark' $qt
else
    warn "Sem $qt — no qt6ct escolhe Style: Darkly e Icon theme: MacTahoe-dark"
end

# 6. Dolphin --------------------------------------------------------------
set -l kw (command -v kwriteconfig6)
if test -n "$kw"
    backup $cfg/dolphinrc
    $kw --file dolphinrc --group General    --key ShowZoomSlider true
    $kw --file dolphinrc --group General    --key ShowStatusBar FullWidth
    $kw --file dolphinrc --group MainWindow --key MenuBar Disabled
    $kw --file dolphinrc --group IconsMode  --key PreviewSize 64
else
    warn "Sem kwriteconfig6 — dolphinrc não alterado"
end

set -l ui $HOME/.local/share/kxmlgui5/dolphin
mkdir -p $ui
backup $ui/dolphinui.rc
cp $repo/kxmlgui/dolphinui.rc $ui/dolphinui.rc

# 7. Ícones personalizados de pastas (config/folder-icons.tsv) ------------
if test -n "$kw"
    for line in (string match -rv '^\s*(#|$)' < $repo/config/folder-icons.tsv)
        set -l parts (string split \t -- $line)
        set -l dir $HOME/$parts[1]
        if test -d $dir
            $kw --file $dir/.directory --group "Desktop Entry" --key Icon $parts[2]
            info "ícone: ~/$parts[1] → $parts[2]"
        end
    end
end

# 8. Primeira recoloração -------------------------------------------------
python3 $cfg/noctalia/scripts/mactahoe-recolor.py

echo
info "Feito. Falta só:"
echo "  • Hyprland: copiar as regras de hypr/dolphin.lua para a tua config"
echo "  • monitor com scale >= 1 (scale < 1 recorta o blur)"
echo "  • fechar e voltar a abrir o Dolphin"
