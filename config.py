# -*- coding: utf-8 -*-
#########################################################################################
#                                                                                       #
#   ██████╗  ██████╗ ██████╗  ██████╗ ███████╗████████╗██╗  ██╗███████╗                 #
#   ██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██║  ██║██╔════╝                 #
#   ██████╔╝██║   ██║██████╔╝██║   ██║█████╗     ██║   ███████║█████╗                   #
#   ██╔══██╗██║   ██║██╔══██╗██║   ██║██╔══╝     ██║   ██╔══██║██╔══╝                   #
#   ██████╔╝╚██████╔╝██████╔╝╚██████╔╝██║        ██║   ██║  ██║███████╗                 #
#   ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝                 #
#   ██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗                                                  #
#   ██║  ██║██╔══██╗██║    ██║██║ ██╔╝                                                  #
#   ███████║███████║██║ █╗ ██║█████╔╝                                                   #
#   ██╔══██║██╔══██║██║███╗██║██╔═██╗                                                   #
#   ██║  ██║██║  ██║╚███╔███╔╝██║  ██╗                                                  # 
#   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝                                                  #
#                                                                                       #
#                         HANDCRAFTED BY BOBOFTHEHAWK                                   #
#                                                                                       #
#########################################################################################
config.load_autoconfig(False)

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

config.set('content.cookies.accept', 'all', 'devtools://*')

config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:136.0) Gecko/20100101 Firefox/139.0', 'https://accounts.google.com/*')

config.set('content.images', True, 'chrome-devtools://*')

config.set('content.images', True, 'devtools://*')

config.set('content.javascript.enabled', True, 'chrome-devtools://*')

config.set('content.javascript.enabled', True, 'devtools://*')

config.set('content.javascript.enabled', True, 'chrome://*/*')

config.set('content.javascript.enabled', True, 'qute://*/*')

config.set('content.local_content_can_access_remote_urls', True, 'file:///home/bob/.local/share/qutebrowser/userscripts/*')

config.set('content.local_content_can_access_file_urls', False, 'file:///home/bob/.local/share/qutebrowser/userscripts/*')

base00 = "#181818"
base01 = "#282828"
base02 = "#383838"
base03 = "#585858"
base04 = "#b8b8b8"
base05 = "#d8d8d8"
base06 = "#e8e8e8"
base07 = "#f8f8f8"
base08 = "#ab4642"
base09 = "#dc9656"
base0A = "#f7ca88"
base0B = "#a1b56c"
base0C = "#86c1b9"
base0D = "#7cafc2"
base0E = "#ba8baf"
base0F = "#a16946"

c.colors.completion.fg = base05

c.colors.completion.odd.bg = base01

c.colors.completion.even.bg = base00

c.colors.completion.category.fg = base0A

c.colors.completion.category.bg = base00

c.colors.completion.category.border.top = base00

c.colors.completion.category.border.bottom = base00

c.colors.completion.item.selected.fg = base05

c.colors.completion.item.selected.bg = base02

c.colors.completion.item.selected.border.top = base02

c.colors.completion.item.selected.border.bottom = base02

c.colors.completion.item.selected.match.fg = base0B

c.colors.completion.match.fg = base0B

c.colors.completion.scrollbar.fg = base05

c.colors.completion.scrollbar.bg = base00

c.colors.contextmenu.disabled.bg = base01

c.colors.contextmenu.disabled.fg = base04

c.colors.contextmenu.menu.bg = base00

c.colors.contextmenu.menu.fg =  base05

c.colors.contextmenu.selected.bg = base02

c.colors.contextmenu.selected.fg = base05

c.colors.downloads.bar.bg = base00

c.colors.downloads.start.fg = base00

c.colors.downloads.start.bg = base0D

c.colors.downloads.stop.fg = base00

c.colors.downloads.stop.bg = base0C

c.colors.downloads.error.fg = base08

c.colors.hints.fg = base00

c.colors.hints.bg = base0A

c.colors.hints.match.fg = base05

c.colors.keyhint.fg = base05

c.colors.keyhint.suffix.fg = base05

c.colors.keyhint.bg = base00

c.colors.messages.error.fg = base00

c.colors.messages.error.bg = base08

c.colors.messages.error.border = base08

c.colors.messages.warning.fg = base00

c.colors.messages.warning.bg = base0E

c.colors.messages.warning.border = base0E

c.colors.messages.info.fg = base05

c.colors.messages.info.bg = base00

c.colors.messages.info.border = base00

c.colors.prompts.fg = base05

c.colors.prompts.border = base00

c.colors.prompts.bg = base00

c.colors.prompts.selected.bg = base02

c.colors.prompts.selected.fg = base05

c.colors.statusbar.normal.fg = base0B

c.colors.statusbar.normal.bg = base00

c.colors.statusbar.insert.fg = base00

c.colors.statusbar.insert.bg = base0D

c.colors.statusbar.passthrough.fg = base00

c.colors.statusbar.passthrough.bg = base0C

c.colors.statusbar.private.fg = base00

c.colors.statusbar.private.bg = base01

c.colors.statusbar.command.fg = base05

c.colors.statusbar.command.bg = base00

c.colors.statusbar.command.private.fg = base05

c.colors.statusbar.command.private.bg = base00

c.colors.statusbar.caret.fg = base00

c.colors.statusbar.caret.bg = base0E

c.colors.statusbar.caret.selection.fg = base00

c.colors.statusbar.caret.selection.bg = base0D

c.colors.statusbar.progress.bg = base0D

c.colors.statusbar.url.fg = base05

c.colors.statusbar.url.error.fg = base08

c.colors.statusbar.url.hover.fg = base05

c.colors.statusbar.url.success.http.fg = base0C

c.colors.statusbar.url.success.https.fg = base0B

c.colors.statusbar.url.warn.fg = base0E

c.colors.tabs.bar.bg = base00

c.colors.tabs.indicator.start = base0D

c.colors.tabs.indicator.stop = base0C

c.colors.tabs.indicator.error = base08

c.colors.tabs.odd.fg = base05

c.colors.tabs.odd.bg = base01

c.colors.tabs.even.fg = base05

c.colors.tabs.even.bg = base00

c.colors.tabs.pinned.even.bg = base0C

c.colors.tabs.pinned.even.fg = base07

c.colors.tabs.pinned.odd.bg = base0B

c.colors.tabs.pinned.odd.fg = base07

c.colors.tabs.pinned.selected.even.bg = base02

c.colors.tabs.pinned.selected.even.fg = base05

c.colors.tabs.pinned.selected.odd.bg = base02

c.colors.tabs.pinned.selected.odd.fg = base05

c.colors.tabs.selected.odd.fg = base05

c.colors.tabs.selected.odd.bg = base02

c.colors.tabs.selected.even.fg = base05

c.colors.tabs.selected.even.bg = base02

c.colors.webpage.darkmode.enabled = True

config.bind('d', 'set-cmd-text -s :tab-close')

c.auto_save.session = True

config.bind('m', 'spawn mpv {url}')

config.bind('M', 'hint links spawn mpv {hint-url}')

config.set('colors.webpage.darkmode.enabled', False, '*://*.youtube.com/*')
config.set('colors.webpage.darkmode.enabled', False, '*://*.youtube-nocookie.com/*')
print("Webpage dark mode for YouTube: DISABLED (use YouTube's native dark theme)")

c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    '!aw':   'https://wiki.archlinux.org/?search={}',
    '!apkg': 'https://archlinux.org/packages/?sort=&q={}',
    '!gh':   'https://github.com/search?o=desc&q={}&s=stars',
    '!yt':   'https://www.youtube.com/results?search_query={}',
    '!r':    'https://www.reddit.com/search?q={}',
    '!so':   'https://stackoverflow.com/search?q={}',
    '!w':    'https://en.wikipedia.org/wiki/Special:Search?search={}',
    '!aur':  'https://aur.archlinux.org/packages?K={}',
    '!g':    'https://www.google.com/search?q={}'
}

# --- ZEN MODE SETTINGS (Initial State: Hidden) ---
config.set('tabs.show', 'switching')
config.set('statusbar.show', 'in-mode')
config.set('scrolling.bar', 'never')

# --- KEYBINDINGS ---
# Press 'zb' to toggle both the Tab bar and Status bar at once
config.bind('zb', 'config-cycle statusbar.show always in-mode ;; config-cycle tabs.show always switching')

# --- File handler ---
config.set('fileselect.handler', 'external')
config.set('fileselect.single_file.command', ['env', 'GTK_THEME=Adwaita:dark', 'zenity', '--file-selection'])
config.set('fileselect.multiple_files.command', ['env', 'GTK_THEME=Adwaita:dark', 'zenity', '--file-selection', '--multiple'])
