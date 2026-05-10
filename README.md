# Qutebrowser Configuration
This repository contains my personal dotfiles for **qutebrowser**, a keyboard-focused browser with a minimal GUI and Vim-like keybindings.

## 📂 Repository Structure
* `config.py`: The main configuration file (Python-based).
* `autoconfig.yml`: Settings modified via the `:set` command within the browser.
* `bookmarks/`: Directory containing saved bookmarks.
* `quickmarks`: List of short-name URL aliases for fast navigation.
* `qsettings/`: Internal browser state and window settings.
* `userscripts/`: Custom userscripts (`highlight`, `highlight-next`, `highlight-prev`).

## 🚀 Installation
To use these configurations, clone this repository into your local qutebrowser config directory (usually `~/.config/qutebrowser`).

### 1. Backup your current config (Optional)
```bash
mv ~/.config/qutebrowser ~/.config/qutebrowser.bak
```

### 2. Clone the repository
```bash
git clone https://github.com/BobOfTheHawk/qutebrowser ~/.config/qutebrowser
```

### 3. Make userscripts executable
```bash
chmod +x ~/.config/qutebrowser/userscripts/*
```

### 4. Launch
Simply start qutebrowser. It will automatically detect the `config.py` file.
```bash
qutebrowser
```

## ⌨️ Key Features & Bindings
* **Vim-like navigation:** Use `h`, `j`, `k`, `l` to scroll.
* **Hinting:** Press `f` to show links and follow them using the keyboard.
* **Quickmarks:** Press `b` to open a bookmark or `M [key]` to set a quickmark.
* **Search:** Use `/` to search within a page.
* **Top and Bottom On,Off:** Use `zb` to hide and unhide.
* **Turn dark mode or light:** Use `td` to turn on or off the dark and light mode.
* **Turn On or Off per one website:** Use `tg` to turn on or off for a specific website.
* **Play video in mpv:** Press `m` on any page, or `M` to hint a specific link.
* **Highlight text:** Select text, press `,h` to highlight in amber.
* **Navigate highlights:** Use `,n` / `,p` to jump forward and backward through highlights.

## 🛠 Customization
If you want to tweak settings, you can edit `config.py` directly. For UI-based changes that persist, use the `:set` command inside qutebrowser, which will update the `autoconfig.yml`.

---

### Tips for a fresh install:
Make sure you have the dependencies installed for your Linux distribution (e.g., `python-adblock` for adblocking features).
Also you need to install zenity that will handle the file selection.

```bash
# Arch Linux
sudo pacman -S qutebrowser python-adblock zenity

# Debian/Ubuntu
sudo apt install qutebrowser zenity
```
