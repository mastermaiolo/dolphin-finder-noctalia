<p align="center">
  <img src="assets/readme/hero.svg" width="100%" alt="dolphin-finder-noctalia — 面向 Hyprland + Noctalia 的 Finder 风格 Dolphin">
</p>

<p align="center"><sub><strong>KDE DOLPHIN · DARKLY · MACTAHOE · HYPRLAND · NOCTALIA</strong></sub></p>

<p align="center">
  <a href="README.md">🇬🇧 English (UK)</a>
  · <a href="README.pt-br.md">🇧🇷 Português (BR)</a>
  · <a href="README.pt-pt.md">🇵🇹 Português (PT)</a>
  · <a href="README.es-es.md">🇪🇸 Español (ES)</a>
  · 🇨🇳 <strong>简体中文</strong>
</p>

> 在 **Hyprland + Noctalia** 上把 Dolphin 打造成 **macOS Finder** 风格:玻璃质感侧边栏、**MacTahoe** 图标,以及**随壁纸变色**的文件夹,跟随 Noctalia 的色调(Material You)调色板。

<p align="center">
  <img src="screenshots/dolphin.png" width="100%" alt="带玻璃侧边栏、MacTahoe 图标和玫瑰色调文件夹的 Dolphin">
</p>

---

## 01 / 概览

<p align="center">
  <img src="assets/readme/at-a-glance.svg" width="100%" alt="Darkly · MacTahoe-dark · Noctalia M3 · Hyprland">
</p>

## 02 / 功能

<p align="center">
  <img src="assets/readme/capabilities.svg" width="100%" alt="功能">
</p>

| 组件 | 作用 |
|---|---|
| **Darkly**(Qt6 样式) | 圆角;半透明侧边栏和工具栏,文件区域带轻微玻璃效果;无焦点线、无分隔线 |
| **MacTahoe-dark**(图标) | macOS Tahoe 风格图标 |
| **Noctalia 模板** + `mactahoe-recolor.py` | 每当配色方案变化,用 Noctalia 的主色调重新着色文件夹 |
| **dolphinrc / dolphinui.rc** | 无菜单栏,精简工具栏(◀ ▶ · 视图 · 路径 · 搜索 · 终端 · 菜单),缩放滑块,64 px 图标 |
| **文件夹图标**(`config/folder-icons.tsv`) | 按文件夹自定义图标(例如 `Vault → folder-sign`) |
| **Hyprland 规则**(`hypr/dolphin.lua`) | 窗口保持不透明(玻璃效果来自 Darkly),对话框浮动 |

### 底层发生了什么?

- 半透明效果由 **Darkly** 按控件绘制。Hyprland 让窗口保持 `opacity 1.0`,只对 Darkly 留出的透明区域做模糊。
- 每次壁纸/配色变化时,Noctalia 根据 M3 配色生成 `palette.json`,然后运行 `post_hook`。
- 该钩子以原始蓝色 SVG(`#006efd`)为基础,重写 `places/scalable` 中的 18 个文件夹 SVG,并清空 KDE 图标缓存。

## 03 / 色调管线

<p align="center">
  <img src="assets/readme/tonal-pipeline.svg" width="100%" alt="wallpaper → M3 → palette.json → mactahoe-recolor.py → icons">
</p>

色相取自 `primary.light`,饱和度取两种主色中更鲜艳的一个(上限为 `MAX_SAT`),亮度固定(`LIGHTNESS`)。文件夹保留壁纸的色相,既不会过于刺眼,也不会发灰。

## 04 / 安装

### 环境要求

- Arch / CachyOS(使用 `paru` 或 `yay`)
- Hyprland(Lua 配置)并启用模糊
- Noctalia Shell,启用 `qt` 和 `kcolorscheme` 模板
- `qt6ct` 作为 platform theme(`QT_QPA_PLATFORMTHEME=qt6ct`)
- `fish`、`git`、`python3`、`kwriteconfig6`

### 快速安装

```fish
git clone https://github.com/mastermaiolo/dolphin-finder-noctalia.git
cd dolphin-finder-noctalia
./install.fish
```

<details>
<summary><strong>安装脚本做了什么</strong></summary>

1. 安装 `darkly`、`inter-font`、`git` 和 `python`(用 `--no-deps` 跳过);
2. 克隆 [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme) 并安装到 `~/.local/share/icons`;
3. 把模板和重新着色脚本复制到 `~/.config/noctalia/`,并在 `config.toml` 中注册模板;
4. 应用 `darklyrc`、`qt6ct`(Darkly + MacTahoe-dark)、`dolphinrc`、工具栏和文件夹图标。

修改任何文件之前都会先备份(`*.bak-YYYYMMDD-HHMMSS`)。

</details>

### 手动步骤

- 把 [`hypr/dolphin.lua`](hypr/dolphin.lua) 中的规则复制到你的 Hyprland 配置;
- 显示器使用 `scale >= 1`(见 *08 / 故障排查*);
- 在 qt6ct 中选择 **Inter 10** 字体;
- 关闭并重新打开 Dolphin。

## 05 / 控制面板

<p align="center">
  <img src="assets/readme/control-surface.svg" width="100%" alt="LIGHTNESS · MAX_SAT · darklyrc">
</p>

立即应用重新着色:

```fish
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py            # Noctalia 颜色
python3 ~/.config/noctalia/scripts/mactahoe-recolor.py '#1a8fe8'  # 固定颜色
```

## 06 / 配置

**文件夹颜色:** 位于 `~/.config/noctalia/scripts/mactahoe-recolor.py` 顶部。

```python
LIGHTNESS = 0.58   # 越低 = 文件夹越暗(Finder ≈ 0.50)
MAX_SAT   = 0.60   # 0.3 = 低调色调 · 0.8 = 鲜艳
```

**玻璃效果:** 位于 `~/.config/darklyrc`。

| 键 | 值 | 效果 |
|---|---|---|
| `DolphinSidebarOpacity` | 55 | 侧边栏(40 = 更通透,70 = 更实) |
| `ToolBarOpacity` | 55 | 工具栏 |
| `DolphinViewOpacity` | 80 | 文件区域(浅色壁纸可调到 85–90) |

<details>
<summary><strong>Noctalia 模板配置块</strong></summary>

由 `install.fish` 添加到 `~/.config/noctalia/config.toml`(或从 `noctalia/config.snippet.toml` 手动添加):

```toml
[theme.templates.user.mactahoe]
input_path = "$HOME/.config/noctalia/templates/mactahoe/palette.json"
output_path = "$HOME/.local/state/mactahoe-noctalia/palette.json"
post_hook = "python3 $HOME/.config/noctalia/scripts/mactahoe-recolor.py"
```

</details>

## 07 / 架构

<p align="center">
  <img src="assets/readme/architecture.svg" width="100%" alt="架构">
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
├── assets/readme/          # README 插图
└── screenshots/
```

## 08 / 故障排查

<p align="center">
  <img src="assets/readme/failure-modes.svg" width="100%" alt="故障排查">
</p>

<details>
<summary><strong>详细说明</strong></summary>

- **窗口底部或右侧的模糊被截断:** 显示器 `scale` 小于 1(例如 `0.9375`)时出现。Hyprland 会在 `宽×scale` / `高×scale` 处截断模糊。解决:`scale = "1"`。
- **侧边栏设备下的容量条:** Dolphin 没有隐藏它们的选项。
- **状态栏中的英文 "16 folders":** 这些字符串在 Dolphin 本身中尚未翻译。
- **文件夹颜色不变:** `post_hook` 没有运行或缺少 `python3` — 手动运行 `mactahoe-recolor.py`。
- **重新安装 MacTahoe** 可能出现 `cannot remove` 警告:无害。

</details>

<details>
<summary><strong>附录 — 卸载</strong></summary>

```fish
rm -rf ~/.local/share/icons/MacTahoe{,-dark,-light} ~/.local/share/mactahoe-noctalia
rm ~/.config/noctalia/scripts/mactahoe-recolor.py
rm -r ~/.config/noctalia/templates/mactahoe
```

然后:

- 从 Noctalia 的 `config.toml` 中删除 `[theme.templates.user.mactahoe]` 配置块;
- 按需恢复 `*.bak-*` 备份文件。

</details>

## 09 / 来源

<p align="center">
  <img src="assets/readme/provenance.svg" width="100%" alt="MacTahoe · Darkly · Noctalia · MIT">
</p>

- [MacTahoe-icon-theme](https://github.com/vinceliuice/MacTahoe-icon-theme),作者 vinceliuice — 安装时下载,本仓库不包含。
- [Darkly](https://github.com/Bali10050/Darkly) — Qt 样式。
- [Noctalia](https://noctalia.dev) — Shell 与模板引擎。

## 10 / 许可证

- 本仓库的脚本与配置:[MIT](LICENSE)。
- MacTahoe-icon-theme:GPL-3.0(上游许可证)。

---

<p align="center"><sub>MAIOLO / SYSTEMS LAB · DFN</sub></p>
