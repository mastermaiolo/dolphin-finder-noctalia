import json
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.abspath(_os.path.join(HERE, "..", ".."))
SW=json.load(open(_os.path.join(HERE,'switch.json')))
CODE_INSTALL='''```fish
git clone https://github.com/<USER>/dolphin-finder-noctalia.git
cd dolphin-finder-noctalia
./install.fish
```'''
CODE_RECOLOR='''```fish
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py            # {a}
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py '#1a8fe8'  # {b}
```'''
CODE_PY='''```python
LIGHTNESS = 0.58   # {a}
MAX_SAT   = 0.60   # {b}
```'''
CODE_TOML='''```toml
[theme.templates.user.mactahoe]
input_path = "$HOME/.config/noctalia/templates/mactahoe/palette.json"
output_path = "$HOME/.local/state/mactahoe-noctalia/palette.json"
post_hook = "python3 $HOME/.config/noctalia/scripts/mactahoe-recolor.py"
```'''
TREE='''```text
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
├── assets/readme/          # {a}
└── screenshots/
```'''
CODE_UN='''```fish
rm -rf ~/.local/share/icons/MacTahoe{,-dark,-light} ~/.local/share/mactahoe-noctalia
rm ~/.config/noctalia/scripts/mactahoe-recolor.py
rm -r ~/.config/noctalia/templates/mactahoe
```'''
def build(k,T):
    rows="\n".join(f"| {a} | {b} |" for a,b in T["pieces"])
    happen="\n".join(f"- {x}" for x in T["happen"])
    req="\n".join(f"- {x}" for x in T["req"])
    inst="\n".join(f"{i+1}. {x}" for i,x in enumerate(T["inst"]))
    man="\n".join(f"- {x}" for x in T["manual"])
    glass="\n".join(f"| `{a}` | {b} | {c} |" for a,b,c in T["glass"])
    fail="\n".join(f"- {x}" for x in T["fail"])
    un="\n".join(f"- {x}" for x in T["un"])
    prov="\n".join(f"- {x}" for x in T["prov"])
    lic="\n".join(f"- {x}" for x in T["lic"])
    h=T["h"]
    return f'''<p align="center">
  <img src="assets/readme/hero.svg" width="100%" alt="dolphin-finder-noctalia — {T["alt_hero"]}">
</p>

<p align="center"><sub><strong>KDE DOLPHIN · DARKLY · MACTAHOE · HYPRLAND · NOCTALIA</strong></sub></p>

{SW[k]}

> {T["lead"]}

<p align="center">
  <img src="screenshots/dolphin.png" width="100%" alt="{T["alt_shot"]}">
</p>

---

## 01 / {h[0]}

<p align="center">
  <img src="assets/readme/at-a-glance.svg" width="100%" alt="Darkly · MacTahoe-dark · Noctalia M3 · Hyprland">
</p>

## 02 / {h[1]}

<p align="center">
  <img src="assets/readme/capabilities.svg" width="100%" alt="{h[1]}">
</p>

| {T["th"][0]} | {T["th"][1]} |
|---|---|
{rows}

### {T["what"]}

{happen}

## 03 / {h[2]}

<p align="center">
  <img src="assets/readme/tonal-pipeline.svg" width="100%" alt="wallpaper → M3 → palette.json → mactahoe-recolor.py → icons">
</p>

{T["pipe"]}

## 04 / {h[3]}

### {T["req_h"]}

{req}

### {T["fast"]}

{CODE_INSTALL.replace("<USER>",T["user"])}

<details>
<summary><strong>{T["inst_h"]}</strong></summary>

{inst}

{T["backup"]}

</details>

### {T["manual_h"]}

{man}

## 05 / {h[4]}

<p align="center">
  <img src="assets/readme/control-surface.svg" width="100%" alt="LIGHTNESS · MAX_SAT · darklyrc">
</p>

{T["now"]}

{CODE_RECOLOR.format(a=T["c_noct"],b=T["c_fixed"])}

## 06 / {h[5]}

{T["fc"]}

{CODE_PY.format(a=T["py_l"],b=T["py_s"])}

{T["gl"]}

| {T["gth"][0]} | {T["gth"][1]} | {T["gth"][2]} |
|---|---|---|
{glass}

<details>
<summary><strong>{T["tb_h"]}</strong></summary>

{T["tb"]}

{CODE_TOML}

</details>

## 07 / {h[6]}

<p align="center">
  <img src="assets/readme/architecture.svg" width="100%" alt="{h[6]}">
</p>

{TREE.format(a=T["art"])}

## 08 / {h[7]}

<p align="center">
  <img src="assets/readme/failure-modes.svg" width="100%" alt="{h[7]}">
</p>

<details>
<summary><strong>{T["long"]}</strong></summary>

{fail}

</details>

<details>
<summary><strong>{T["un_h"]}</strong></summary>

{CODE_UN}

{T["then"]}

{un}

</details>

## 09 / {h[8]}

<p align="center">
  <img src="assets/readme/provenance.svg" width="100%" alt="MacTahoe · Darkly · Noctalia · MIT">
</p>

{prov}

## 10 / {h[9]}

{lic}

---

<p align="center"><sub>MAIOLO / SYSTEMS LAB · DFN</sub></p>
'''
L=json.load(open(_os.path.join(HERE,'lang.json')))
names={"en":"README.md","pt-br":"README.pt-br.md","pt-pt":"README.pt-pt.md","es-es":"README.es-es.md","zh-cn":"README.zh-cn.md"}
for k,T in L.items(): open(_os.path.join(ROOT,names[k]),"w").write(build(k,T))
print("built",list(L))
