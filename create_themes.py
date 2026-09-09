#!/usr/bin/env python3
import json
import os

THEMES_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_THEMES = [
    {"name": "monokai-pro-octagon", "desc": "Monokai Pro Octagon", "primary": "#FC9867", "primaryContainer": "#6A4E2D", "onPrimaryContainer": "#FFFCF2", "secondary": "#A9DC76", "tertiary": "#AB9DF2", "onSecondaryContainer": "#E8F5D8", "surface": "#1A1A2E", "surfaceDim": "#12121E", "surfaceContainerLow": "#22223A", "onSecondaryFixed": "#3A5020"},
    {"name": "monokai-pro-ristretto", "desc": "Monokai Pro Ristretto", "primary": "#FC9678", "primaryContainer": "#6A3E2D", "onPrimaryContainer": "#FFF0E8", "secondary": "#A9DC76", "tertiary": "#AB9DF2", "onSecondaryContainer": "#E8F5D8", "surface": "#1C1816", "surfaceDim": "#141210", "surfaceContainerLow": "#262220", "onSecondaryFixed": "#3A5020"},
    {"name": "tokyo-night-storm", "desc": "Tokyo Night Storm", "primary": "#7AA2F7", "primaryContainer": "#1E3A5F", "onPrimaryContainer": "#C0D0F0", "secondary": "#9ECE6A", "tertiary": "#FF9E64", "onSecondaryContainer": "#D8F0D0", "surface": "#1A1B26", "surfaceDim": "#13141C", "surfaceContainerLow": "#222330", "onSecondaryFixed": "#1A4020"},
    {"name": "tokyo-night-light", "desc": "Tokyo Night Light", "primary": "#34548A", "primaryContainer": "#A0B0D0", "onPrimaryContainer": "#1A1B26", "secondary": "#4C7A3E", "tertiary": "#8C5530", "onSecondaryContainer": "#E8F0E0", "surface": "#E1E2E7", "surfaceDim": "#D0D1D6", "surfaceContainerLow": "#EAEAF0", "onSecondaryFixed": "#2A4020"},
    {"name": "catppuccin-latte", "desc": "Catppuccin Latte", "primary": "#8839EF", "primaryContainer": "#DCC0FF", "onPrimaryContainer": "#3B1F6A", "secondary": "#179299", "tertiary": "#E64553", "onSecondaryContainer": "#C0F0F0", "surface": "#EFF1F5", "surfaceDim": "#DCE0E8", "surfaceContainerLow": "#F5F5FA", "onSecondaryFixed": "#005060"},
    {"name": "catppuccin-frappe", "desc": "Catppuccin Frappe", "primary": "#CA9EE6", "primaryContainer": "#5B3D7A", "onPrimaryContainer": "#F0E0FF", "secondary": "#81C8BE", "tertiary": "#EA999C", "onSecondaryContainer": "#D8F0EC", "surface": "#303446", "surfaceDim": "#232634", "surfaceContainerLow": "#3A3E50", "onSecondaryFixed": "#1A5048"},
    {"name": "catppuccin-macchiato", "desc": "Catppuccin Macchiato", "primary": "#C6A0F6", "primaryContainer": "#5B3D7A", "onPrimaryContainer": "#F0E0FF", "secondary": "#8BD5CA", "tertiary": "#EE99A0", "onSecondaryContainer": "#D8F0EC", "surface": "#24273A", "surfaceDim": "#181A26", "surfaceContainerLow": "#2E3146", "onSecondaryFixed": "#1A5048"},
    {"name": "dracula-soft", "desc": "Dracula Soft", "primary": "#BD93F9", "primaryContainer": "#4A3570", "onPrimaryContainer": "#F0E8FF", "secondary": "#50FA7B", "tertiary": "#FFB86C", "onSecondaryContainer": "#D0FFE0", "surface": "#282A36", "surfaceDim": "#1E202C", "surfaceContainerLow": "#32344A", "onSecondaryFixed": "#1A5030"},
    {"name": "dracula-midnight", "desc": "Dracula Midnight", "primary": "#B39DDB", "primaryContainer": "#3E3060", "onPrimaryContainer": "#E8E0F8", "secondary": "#80CBC4", "tertiary": "#FFCC80", "onSecondaryContainer": "#D0F0EC", "surface": "#191A24", "surfaceDim": "#10111A", "surfaceContainerLow": "#222330", "onSecondaryFixed": "#1A4A40"},
    {"name": "nord-polar-night", "desc": "Nord Polar Night", "primary": "#88C0D0", "primaryContainer": "#2E4050", "onPrimaryContainer": "#D0E8F0", "secondary": "#A3BE8C", "tertiary": "#EBCB8B", "onSecondaryContainer": "#E0F0D8", "surface": "#2E3440", "surfaceDim": "#242830", "surfaceContainerLow": "#3A3E4A", "onSecondaryFixed": "#2A4A20"},
    {"name": "nord-aurora", "desc": "Nord Aurora", "primary": "#81A1C1", "primaryContainer": "#3B4A60", "onPrimaryContainer": "#D0E0F0", "secondary": "#A3BE8C", "tertiary": "#EBCB8B", "onSecondaryContainer": "#E0F0D8", "surface": "#2E3440", "surfaceDim": "#242830", "surfaceContainerLow": "#3A3E4A", "onSecondaryFixed": "#2A4A20"},
    {"name": "gruvbox-light", "desc": "Gruvbox Light", "primary": "#B8BB26", "primaryContainer": "#505820", "onPrimaryContainer": "#F0F8D0", "secondary": "#FABD2F", "tertiary": "#FE8019", "onSecondaryContainer": "#FFF0C0", "surface": "#FBF1C7", "surfaceDim": "#E8DDA8", "surfaceContainerLow": "#FFF8E0", "onSecondaryFixed": "#504010"},
    {"name": "gruvbox-dark-hard", "desc": "Gruvbox Dark Hard", "primary": "#FB4934", "primaryContainer": "#7A2018", "onPrimaryContainer": "#FFD0C8", "secondary": "#B8BB26", "tertiary": "#FABD2F", "onSecondaryContainer": "#E8F8D0", "surface": "#1D2021", "surfaceDim": "#151718", "surfaceContainerLow": "#282A2B", "onSecondaryFixed": "#505820"},
    {"name": "gruvbox-dark-medium", "desc": "Gruvbox Dark Medium", "primary": "#FB4934", "primaryContainer": "#7A2018", "onPrimaryContainer": "#FFD0C8", "secondary": "#B8BB26", "tertiary": "#FABD2F", "onSecondaryContainer": "#E8F8D0", "surface": "#282828", "surfaceDim": "#1D1D1D", "surfaceContainerLow": "#333333", "onSecondaryFixed": "#505820"},
    {"name": "solarized-dark-higher", "desc": "Solarized Dark Higher Contrast", "primary": "#268BD2", "primaryContainer": "#104870", "onPrimaryContainer": "#B0D8F8", "secondary": "#859900", "tertiary": "#CB4B16", "onSecondaryContainer": "#D8F0C0", "surface": "#002B36", "surfaceDim": "#001E26", "surfaceContainerLow": "#003846", "onSecondaryFixed": "#2A5010"},
    {"name": "solarized-light-higher", "desc": "Solarized Light Higher Contrast", "primary": "#268BD2", "primaryContainer": "#90C8E8", "onPrimaryContainer": "#003050", "secondary": "#859900", "tertiary": "#CB4B16", "onSecondaryContainer": "#D8F0C0", "surface": "#FDF6E3", "surfaceDim": "#E8DEC8", "surfaceContainerLow": "#FFF8F0", "onSecondaryFixed": "#2A5010"},
    {"name": "material-ocean", "desc": "Material Ocean", "primary": "#82AAFF", "primaryContainer": "#2A4070", "onPrimaryContainer": "#D0E0FF", "secondary": "#C3E88D", "tertiary": "#F07178", "onSecondaryContainer": "#E0F8D0", "surface": "#1A2030", "surfaceDim": "#121820", "surfaceContainerLow": "#222A3A", "onSecondaryFixed": "#2A5020"},
    {"name": "material-palenight", "desc": "Material Palenight", "primary": "#C792EA", "primaryContainer": "#4A3070", "onPrimaryContainer": "#F0E0FF", "secondary": "#C3E88D", "tertiary": "#FFCB6B", "onSecondaryContainer": "#E0F8D0", "surface": "#1E2030", "surfaceDim": "#161820", "surfaceContainerLow": "#282A3A", "onSecondaryFixed": "#2A5020"},
    {"name": "material-darker", "desc": "Material Darker", "primary": "#82AAFF", "primaryContainer": "#2A4070", "onPrimaryContainer": "#D0E0FF", "secondary": "#C3E88D", "tertiary": "#FF5370", "onSecondaryContainer": "#E0F8D0", "surface": "#101218", "surfaceDim": "#0A0C10", "surfaceContainerLow": "#1A1C24", "onSecondaryFixed": "#2A5020"},
    {"name": "oceanic-next-dark", "desc": "Oceanic Next Dark", "primary": "#C594C5", "primaryContainer": "#5A3A5A", "onPrimaryContainer": "#F0E0F0", "secondary": "#99C794", "tertiary": "#FAC863", "onSecondaryContainer": "#E0F8E0", "surface": "#1C2028", "surfaceDim": "#141820", "surfaceContainerLow": "#242A34", "onSecondaryFixed": "#2A4A20"},
    {"name": "palenight-github", "desc": "GitHub Palenight", "primary": "#79B8FF", "primaryContainer": "#2A4A78", "onPrimaryContainer": "#D0E8FF", "secondary": "#B392F0", "tertiary": "#FFAB70", "onSecondaryContainer": "#E8E0FF", "surface": "#24292E", "surfaceDim": "#1A1E24", "surfaceContainerLow": "#303640", "onSecondaryFixed": "#2A3060"},
    {"name": "one-dark-pro", "desc": "One Dark Pro", "primary": "#61AFEF", "primaryContainer": "#2A4A78", "onPrimaryContainer": "#D0E8FF", "secondary": "#98C379", "tertiary": "#E5C07B", "onSecondaryContainer": "#E0F8D0", "surface": "#282C34", "surfaceDim": "#1E2228", "surfaceContainerLow": "#343A44", "onSecondaryFixed": "#2A5020"},
    {"name": "one-dark-vivid", "desc": "One Dark Vivid", "primary": "#61AFEF", "primaryContainer": "#2A4A78", "onPrimaryContainer": "#D0E8FF", "secondary": "#56B6C2", "tertiary": "#E5C07B", "onSecondaryContainer": "#C0F0F0", "surface": "#282C34", "surfaceDim": "#1E2228", "surfaceContainerLow": "#343A44", "onSecondaryFixed": "#1A4A48"},
    {"name": "ayu-dark", "desc": "Ayu Dark", "primary": "#E6B450", "primaryContainer": "#6A4E20", "onPrimaryContainer": "#FFF0D0", "secondary": "#BFBDB0", "tertiary": "#E6B450", "onSecondaryContainer": "#F0F0E8", "surface": "#0D1017", "surfaceDim": "#080A0E", "surfaceContainerLow": "#141820", "onSecondaryFixed": "#504820"},
    {"name": "ayu-light", "desc": "Ayu Light", "primary": "#FF8F40", "primaryContainer": "#7A4020", "onPrimaryContainer": "#FFF0E0", "secondary": "#8A8A8A", "tertiary": "#FF8F40", "onSecondaryContainer": "#F0F0F0", "surface": "#FAFAFA", "surfaceDim": "#E8E8E8", "surfaceContainerLow": "#FFFFFF", "onSecondaryFixed": "#404040"},
    {"name": "ayu-mirage-pure", "desc": "Ayu Mirage Pure", "primary": "#FFCC66", "primaryContainer": "#7A5A20", "onPrimaryContainer": "#FFF8E0", "secondary": "#BFBDB0", "tertiary": "#FFCC66", "onSecondaryContainer": "#F0F0E8", "surface": "#1F2430", "surfaceDim": "#161A22", "surfaceContainerLow": "#282E3A", "onSecondaryFixed": "#504820"},
    {"name": "monochrome-dark", "desc": "Monochrome Dark", "primary": "#FFFFFF", "primaryContainer": "#404040", "onPrimaryContainer": "#FFFFFF", "secondary": "#CCCCCC", "tertiary": "#999999", "onSecondaryContainer": "#F0F0F0", "surface": "#121212", "surfaceDim": "#0A0A0A", "surfaceContainerLow": "#1C1C1C", "onSecondaryFixed": "#383838"},
    {"name": "github-dark-default", "desc": "GitHub Dark Default", "primary": "#58A6FF", "primaryContainer": "#1F3D5C", "onPrimaryContainer": "#C8E0FF", "secondary": "#3FB950", "tertiary": "#D29922", "onSecondaryContainer": "#C8F0D0", "surface": "#0D1117", "surfaceDim": "#080C10", "surfaceContainerLow": "#161C24", "onSecondaryFixed": "#1A5020"},
    {"name": "github-dark-dimmed", "desc": "GitHub Dark Dimmed", "primary": "#58A6FF", "primaryContainer": "#1F3D5C", "onPrimaryContainer": "#C8E0FF", "secondary": "#3FB950", "tertiary": "#D29922", "onSecondaryContainer": "#C8F0D0", "surface": "#24292F", "surfaceDim": "#1A1E24", "surfaceContainerLow": "#2E3440", "onSecondaryFixed": "#1A5020"},
    {"name": "github-light-default", "desc": "GitHub Light Default", "primary": "#0969DA", "primaryContainer": "#A8D0F0", "onPrimaryContainer": "#003060", "secondary": "#1A7F37", "tertiary": "#9A6700", "onSecondaryContainer": "#C8F0D0", "surface": "#FFFFFF", "surfaceDim": "#E8E8E8", "surfaceContainerLow": "#F8F8F8", "onSecondaryFixed": "#1A5020"},
    {"name": "github-light-high-contrast", "desc": "GitHub Light High Contrast", "primary": "#0550AE", "primaryContainer": "#88C0F0", "onPrimaryContainer": "#002050", "secondary": "#116329", "tertiary": "#7A5500", "onSecondaryContainer": "#C8F0D0", "surface": "#FFFFFF", "surfaceDim": "#F0F0F0", "surfaceContainerLow": "#FFFFFF", "onSecondaryFixed": "#1A4020"},
    {"name": "synthwave-84", "desc": "Synthwave '84", "primary": "#F92AAD", "primaryContainer": "#6A1050", "onPrimaryContainer": "#FFB0E0", "secondary": "#FED73E", "tertiary": "#36F9F6", "onSecondaryContainer": "#FFF8C8", "surface": "#241B30", "surfaceDim": "#1A1224", "surfaceContainerLow": "#2E2440", "onSecondaryFixed": "#5A4A10"},
    {"name": "nightfox", "desc": "Nightfox", "primary": "#59C2FF", "primaryContainer": "#1E4A6A", "onPrimaryContainer": "#C0E8FF", "secondary": "#7BD88F", "tertiary": "#FFAD66", "onSecondaryContainer": "#D0F0D8", "surface": "#192330", "surfaceDim": "#101820", "surfaceContainerLow": "#222C3A", "onSecondaryFixed": "#1A5030"},
    {"name": "dayfox", "desc": "Dayfox", "primary": "#2D6CF6", "primaryContainer": "#1A4A8A", "onPrimaryContainer": "#D0E0FF", "secondary": "#397E47", "tertiary": "#B05D00", "onSecondaryContainer": "#D0F0D8", "surface": "#F6F2EF", "surfaceDim": "#E0DCD8", "surfaceContainerLow": "#FFFAF8", "onSecondaryFixed": "#1A4020"},
    {"name": "duskfox", "desc": "Duskfox", "primary": "#AD6AFF", "primaryContainer": "#4A2A78", "onPrimaryContainer": "#F0E0FF", "secondary": "#6AD99C", "tertiary": "#F4A640", "onSecondaryContainer": "#D8F8E0", "surface": "#29373E", "surfaceDim": "#1E2A30", "surfaceContainerLow": "#344450", "onSecondaryFixed": "#1A5040"},
    {"name": "nordfox", "desc": "Nordfox", "primary": "#7EB8DA", "primaryContainer": "#2A4A60", "onPrimaryContainer": "#D0E8F8", "secondary": "#8CCF8C", "tertiary": "#E0C080", "onSecondaryContainer": "#D8F8D8", "surface": "#2A3440", "surfaceDim": "#202830", "surfaceContainerLow": "#343E4A", "onSecondaryFixed": "#1A5030"},
    {"name": "terafox", "desc": "Terafox", "primary": "#5FC4E8", "primaryContainer": "#1E5A70", "onPrimaryContainer": "#C0E8F8", "secondary": "#7BD88F", "tertiary": "#FFAD66", "onSecondaryContainer": "#D0F0D8", "surface": "#192028", "surfaceDim": "#101820", "surfaceContainerLow": "#222C38", "onSecondaryFixed": "#1A5030"},
    {"name": "carbonfox", "desc": "Carbonfox", "primary": "#6E9FDA", "primaryContainer": "#2A4A6A", "onPrimaryContainer": "#D0E8FF", "secondary": "#91D198", "tertiary": "#FFB070", "onSecondaryContainer": "#D8F8E0", "surface": "#161616", "surfaceDim": "#0E0E0E", "surfaceContainerLow": "#1E1E1E", "onSecondaryFixed": "#1A5030"},
    {"name": "nightowl-light", "desc": "Night Owl Light", "primary": "#0184BC", "primaryContainer": "#005070", "onPrimaryContainer": "#A0D8F0", "secondary": "#72B03D", "tertiary": "#E5C07B", "onSecondaryContainer": "#D8F0D0", "surface": "#FBFCFF", "surfaceDim": "#E0E4EA", "surfaceContainerLow": "#FFFFFF", "onSecondaryFixed": "#1A5020"},
    {"name": "rose-pine-dawn", "desc": "Rosé Pine Dawn", "primary": "#907AA9", "primaryContainer": "#4A3A5A", "onPrimaryContainer": "#F0E0FF", "secondary": "#56949F", "tertiary": "#EA9A97", "onSecondaryContainer": "#D8F0F0", "surface": "#FAF4ED", "surfaceDim": "#E0DCD8", "surfaceContainerLow": "#FFFAF8", "onSecondaryFixed": "#1A4A4A"},
    {"name": "rose-pine-moon", "desc": "Rosé Pine Moon", "primary": "#C4A7E7", "primaryContainer": "#5A3A70", "onPrimaryContainer": "#F0E0FF", "secondary": "#9CCFD8", "tertiary": "#F6C177", "onSecondaryContainer": "#D8F8FF", "surface": "#232136", "surfaceDim": "#1A1824", "surfaceContainerLow": "#2E2C3E", "onSecondaryFixed": "#1A4A5A"},
    {"name": "kanagawa-dragon", "desc": "Kanagawa Dragon", "primary": "#7FB4CA", "primaryContainer": "#2A4A5A", "onPrimaryContainer": "#D0E8F0", "secondary": "#957FB8", "tertiary": "#DCA561", "onSecondaryContainer": "#E8E0F8", "surface": "#16161D", "surfaceDim": "#0E0E14", "surfaceContainerLow": "#1E1E28", "onSecondaryFixed": "#3A2A50"},
    {"name": "kanagawa-lotus", "desc": "Kanagawa Lotus", "primary": "#4D6A8E", "primaryContainer": "#1A3A5A", "onPrimaryContainer": "#D0E0F8", "secondary": "#6F89AA", "tertiary": "#C49A6C", "onSecondaryContainer": "#E0E8F0", "surface": "#181818", "surfaceDim": "#101010", "surfaceContainerLow": "#202020", "onSecondaryFixed": "#2A3A50"},
    {"name": "everforest-medium", "desc": "Everforest Medium", "primary": "#A7C080", "primaryContainer": "#3A5028", "onPrimaryContainer": "#E0F8D0", "secondary": "#D39BB6", "tertiary": "#7FBBB3", "onSecondaryContainer": "#F8E0F0", "surface": "#2D353B", "surfaceDim": "#222A30", "surfaceContainerLow": "#384248", "onSecondaryFixed": "#5A3050"},
    {"name": "everforest-light", "desc": "Everforest Light", "primary": "#8DA101", "primaryContainer": "#3A5008", "onPrimaryContainer": "#E0F8D0", "secondary": "#C17E70", "tertiary": "#35A77A", "onSecondaryContainer": "#F8E0D8", "surface": "#F1F0E9", "surfaceDim": "#E0DED8", "surfaceContainerLow": "#FAFAF8", "onSecondaryFixed": "#5A2018"},
    {"name": "kanagawa-wave", "desc": "Kanagawa Wave", "primary": "#7E9CD8", "primaryContainer": "#2A3A60", "onPrimaryContainer": "#D0E0FF", "secondary": "#957FB8", "tertiary": "#DCA561", "onSecondaryContainer": "#E8E0F8", "surface": "#1F1F2E", "surfaceDim": "#161620", "surfaceContainerLow": "#28283A", "onSecondaryFixed": "#3A2A50"},
    {"name": "modus-operandi", "desc": "Modus Operandi", "primary": "#005FB7", "primaryContainer": "#003A70", "onPrimaryContainer": "#B0D4F8", "secondary": "#00803F", "tertiary": "#813E90", "onSecondaryContainer": "#C0F0D0", "surface": "#F8F8F8", "surfaceDim": "#E0E0E0", "surfaceContainerLow": "#FFFFFF", "onSecondaryFixed": "#004020"},
    {"name": "modus-vivendi", "desc": "Modus Vivendi", "primary": "#00BCFF", "primaryContainer": "#005A80", "onPrimaryContainer": "#B0E8FF", "secondary": "#00CF60", "tertiary": "#D080FF", "onSecondaryContainer": "#C0FFE0", "surface": "#1D1D22", "surfaceDim": "#141418", "surfaceContainerLow": "#262630", "onSecondaryFixed": "#005030"},
    {"name": "vscode-default-dark", "desc": "VSCode Default Dark+", "primary": "#569CD6", "primaryContainer": "#1E3A5A", "onPrimaryContainer": "#C8E0FF", "secondary": "#4EC9B0", "tertiary": "#DCDCAA", "onSecondaryContainer": "#C0F8F0", "surface": "#1E1E1E", "surfaceDim": "#161616", "surfaceContainerLow": "#252526", "onSecondaryFixed": "#1A5048"},
    {"name": "vscode-default-light", "desc": "VSCode Default Light+", "primary": "#0451A5", "primaryContainer": "#A0C8F0", "onPrimaryContainer": "#002A5A", "secondary": "#007A8A", "tertiary": "#795E26", "onSecondaryContainer": "#C0F0F0", "surface": "#FFFFFF", "surfaceDim": "#E8E8E8", "surfaceContainerLow": "#F8F8F8", "onSecondaryFixed": "#003A40"},
    {"name": "tokyo-night-color", "desc": "Tokyo Night Color", "primary": "#BB9AF7", "primaryContainer": "#4A2A70", "onPrimaryContainer": "#F0E0FF", "secondary": "#73DACA", "tertiary": "#FF9E64", "onSecondaryContainer": "#D8FFF0", "surface": "#1A1B26", "surfaceDim": "#13141C", "surfaceContainerLow": "#222330", "onSecondaryFixed": "#1A5050"},
    {"name": "material-theme-oceanic", "desc": "Material Theme Oceanic", "primary": "#546E7A", "primaryContainer": "#263238", "onPrimaryContainer": "#C0D8E0", "secondary": "#C3E88D", "tertiary": "#FFCB6B", "onSecondaryContainer": "#E0F8D0", "surface": "#263238", "surfaceDim": "#1C262C", "surfaceContainerLow": "#303C44", "onSecondaryFixed": "#2A5020"},
    {"name": "one-light-vivid", "desc": "One Light Vivid", "primary": "#4078F2", "primaryContainer": "#1A4A8A", "onPrimaryContainer": "#D0E0FF", "secondary": "#50A14F", "tertiary": "#C18401", "onSecondaryContainer": "#D8F0D0", "surface": "#FAFAFA", "surfaceDim": "#E8E8E8", "surfaceContainerLow": "#FFFFFF", "onSecondaryFixed": "#1A4020"},
    {"name": "high-contrast-dark", "desc": "High Contrast Dark", "primary": "#FFFFFF", "primaryContainer": "#404040", "onPrimaryContainer": "#FFFFFF", "secondary": "#FFD700", "tertiary": "#00FFFF", "onSecondaryContainer": "#FFF8C0", "surface": "#000000", "surfaceDim": "#000000", "surfaceContainerLow": "#1A1A1A", "onSecondaryFixed": "#5A5000"},
    {"name": "dracula-jetbrains", "desc": "JetBrains Dracula — official Dracula for JetBrains IDEs", "primary": "#BD93F9", "primaryContainer": "#4A3570", "onPrimaryContainer": "#F0E8FF", "secondary": "#50FA7B", "tertiary": "#FFB86C", "onSecondaryContainer": "#D0FFE0", "surface": "#282A36", "surfaceDim": "#1E202C", "surfaceContainerLow": "#32344A", "onSecondaryFixed": "#1A5030"},
]


def create_theme(theme_info):
    name = theme_info["name"]
    p = theme_info["primary"]
    pc = theme_info["primaryContainer"]
    opc = theme_info["onPrimaryContainer"]
    s = theme_info["secondary"]
    t = theme_info["tertiary"]
    osc = theme_info["onSecondaryContainer"]
    sf = theme_info["surface"]
    sd = theme_info["surfaceDim"]
    scl = theme_info["surfaceContainerLow"]
    osf = theme_info["onSecondaryFixed"]

    data = {
        "activity": {"background": sf, "statusBar": sf, "navigationBar": sf},
        "editor": {
            "lineDivider": scl, "wholeBackground": sf, "lineNumber": osf,
            "lineNumberBackground": sf, "textNormal": opc, "keyword": p,
            "comment": osf, "operator": s, "literal": t, "identifierVar": opc,
            "identifierName": opc, "functionName": p, "annotation": t,
            "htmlTag": p, "attributeName": s, "attributeValue": t,
            "nonPrintableChar": osf, "colornextdot": p, "colornextbrak": s,
            "colornextchar": t, "coloruppercase": p, "colornextless": s,
            "currentLine": scl, "currentRowBorder": scl, "blockLine": scl,
            "blockLineCurrent": p, "sideBlockLine": scl, "hardWrapMarker": scl,
            "strikeThrough": "#00000000", "lineNumberCurrent": p,
            "selectedTextBackground": scl, "selectedTextBorder": p,
            "textSelected": opc, "selectionInsert": p, "selectionHandle": p,
            "underline": p, "scrollBarThumb": scl, "scrollBarThumbPressed": p,
            "scrollBarTrack": sd, "completionWndBackground": sf,
            "completionWndCorner": sf, "completionWndTextPrimary": opc,
            "completionWndTextSecondary": osf, "completionWndItemCurrent": scl,
            "completionWndTextMatched": p, "matchedTextBackground": scl,
            "matchedTextBorder": p, "highlightedDelimitersBackground": scl,
            "highlightedDelimitersUnderline": p, "highlightedDelimitersForeground": opc,
            "highlightedDelimitersBorder": p, "textHighlightBackground": scl,
            "textHighlightBorder": p, "textHighlightStrongBackground": scl,
            "textHighlightStrongBorder": s, "staticSpanBackground": sf,
            "staticSpanForeground": opc, "problemError": "#F07178",
            "problemWarning": "#FFB74D", "problemTypo": t,
            "signatureBackground": sf, "signatureBorder": scl,
            "signatureTextNormal": opc, "signatureTextHighlightedParameter": p,
            "hoverBackground": scl, "hoverBorder": scl, "hoverTextNormal": opc,
            "hoverTextHighlighted": p, "diagnosticTooltipBackground": sf,
            "diagnosticTooltipBriefMsg": opc, "diagnosticTooltipDetailedMsg": osf,
            "diagnosticTooltipAction": p, "textActionWindowBackground": sf,
            "textActionWindowIconColor": opc, "textInlayHintBackground": sf,
            "textInlayHintForeground": osf, "snippetBackgroundEditing": scl,
            "snippetBackgroundRelated": scl, "snippetBackgroundInactive": sf,
            "functionCharBackgroundStroke": s, "minimapBackground": sd,
            "minimapViewport": "#30ffffff", "minimapViewportBorder": "#b0ffffff",
            "bracketlevelmatch1": p, "bracketlevelmatch2": s, "bracketlevelmatch3": t,
            "bracketlevelmatch4": opc, "bracketlevelmatch5": osf, "bracketlevelmatch6": p,
            "stickyScrollDivider": scl
        },
        "widget": {
            "text": opc, "hint": osf, "accent": p, "background": sf,
            "surface": scl, "stroke": scl, "fabBackground": p, "fabIcon": sf,
            "tabSelected": p, "tabUnselected": osf, "imageTint": opc,
            "menubackground": sd, "menutextcolor": opc, "selectedmenucolor": scl,
            "imagepath": "", "blursize": 1
        },
        "material3": {
            "primary": p, "surfaceTint": p, "onPrimary": sf, "primaryContainer": pc,
            "onPrimaryContainer": opc, "secondary": s, "onSecondary": sf,
            "secondaryContainer": scl, "onSecondaryContainer": osc,
            "tertiary": t, "onTertiary": sf, "tertiaryContainer": scl,
            "onTertiaryContainer": osc, "error": "#F07178", "onError": "#602D30",
            "errorContainer": "#843E42", "onErrorContainer": "#F9C6C9",
            "background": sf, "onBackground": opc, "surface": sf,
            "onSurface": opc, "surfaceVariant": scl, "onSurfaceVariant": opc,
            "outline": osf, "outlineVariant": scl, "shadow": "#000000",
            "scrim": "#000000", "inverseSurface": opc, "inverseOnSurface": sf,
            "inversePrimary": pc, "primaryFixed": opc, "onPrimaryFixed": pc,
            "primaryFixedDim": p, "onPrimaryFixedVariant": pc,
            "secondaryFixed": osc, "onSecondaryFixed": osf,
            "secondaryFixedDim": s, "onSecondaryFixedVariant": osf,
            "tertiaryFixed": osc, "onTertiaryFixed": osf,
            "tertiaryFixedDim": t, "onTertiaryFixedVariant": osf,
            "surfaceDim": sd, "surfaceBright": scl, "surfaceContainerLowest": sd,
            "surfaceContainerLow": scl, "surfaceContainer": scl,
            "surfaceContainerHigh": scl, "surfaceContainerHighest": scl
        }
    }

    theme_dir = os.path.join(THEMES_DIR, name)
    os.makedirs(theme_dir, exist_ok=True)
    with open(os.path.join(theme_dir, f"{name}.gth"), "w") as f:
        json.dump(data, f, indent=2)

    readme = f"# {name.replace('-', ' ').title()}\n\n{theme_info['desc']}\n\n## Apply\n1. Open `{name}.gth` in the File Manager.\n2. Tap **Apply**.\n"
    with open(os.path.join(theme_dir, "readme.md"), "w") as f:
        f.write(readme)

    return {"name": name, "icon": "", "doc": f"https://raw.githubusercontent.com/HanzoDev1375/ghostidetheme/main/{name}/readme.md", "version": 1, "devname": "ghost", "linkdownload": f"https://raw.githubusercontent.com/HanzoDev1375/ghostidetheme/main/{name}/{name}.gth"}


def main():
    import sys
    filters = sys.argv[1:]

    created = []
    for t in NEW_THEMES:
        if filters and t["name"] not in filters:
            continue
        entry = create_theme(t)
        created.append(entry)
        print(f"  [+] {t['name']} — {t['desc']}")

    with open(os.path.join(THEMES_DIR, "theme.json"), "r") as f:
        themes = json.load(f)
    existing = {t["name"] for t in themes}
    for c in created:
        if c["name"] not in existing:
            themes.append(c)
    with open(os.path.join(THEMES_DIR, "theme.json"), "w") as f:
        json.dump(themes, f, indent=2)

    print(f"\nCreated {len(created)} themes. Total: {len(themes)}")


if __name__ == "__main__":
    main()
