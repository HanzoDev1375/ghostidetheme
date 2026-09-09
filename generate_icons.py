#!/usr/bin/env python3
import json
import os
import re
from PIL import Image, ImageDraw
import cairosvg
import io

THEMES_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_PATH = os.path.join(THEMES_DIR, "icon", "color_lens_s1.svg")
BG_PATH = os.path.join(THEMES_DIR, "icon", "background.png")
ICON_SIZE = 512
CORNER_RADIUS = 0.30


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def is_valid_hex(h):
    if not h or not h.startswith("#"):
        return False
    h = h.lstrip("#")
    return len(h) == 6 and all(c in "0123456789abcdefABCDEF" for c in h)


def resolve_ref(val, data):
    if not isinstance(val, str) or not val.startswith("@"):
        return val
    parts = val[1:].split(".")
    obj = data
    for p in parts:
        if isinstance(obj, dict) and p in obj:
            obj = obj[p]
        else:
            return val
    return resolve_ref(obj, data) if isinstance(obj, str) else val


def get_color(data, section, key, default):
    val = data.get(section, {}).get(key, default)
    val = resolve_ref(val, data)
    if is_valid_hex(val):
        return val
    return default


def make_gradient(w, h, colors):
    valid = [c for c in colors if is_valid_hex(c)]
    if len(valid) < 2:
        valid = [default for default in ["#0e0e12", "#101014", "#1a1a1d", "#45d6ff"][:len(colors)]]
    n = len(valid)
    rgb_list = [hex_to_rgb(c) for c in valid]
    img = Image.new("RGB", (w, h))
    pixels = img.load()
    for y in range(h):
        for x in range(w):
            t = (x / (w - 1) + y / (h - 1)) / 2.0
            seg = t * (n - 1)
            i = min(int(seg), n - 2)
            local_t = seg - i
            r = int(rgb_list[i][0] + (rgb_list[i + 1][0] - rgb_list[i][0]) * local_t)
            g = int(rgb_list[i][1] + (rgb_list[i + 1][1] - rgb_list[i][1]) * local_t)
            b = int(rgb_list[i][2] + (rgb_list[i + 1][2] - rgb_list[i][2]) * local_t)
            pixels[x, y] = (r, g, b)
    return img


def apply_rounded_corners(img, radius_pct):
    w, h = img.size
    radius = int(min(w, h) * radius_pct)
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), (w - 1, h - 1)], radius=radius, fill=255)
    result = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    result.paste(img.convert("RGBA"), mask=mask)
    return result


def render_multicolor_svg(svg_path, size, lens_color, circle_colors):
    with open(svg_path, "r") as f:
        svg_data = f.read()

    paths = re.findall(r'<path\s+d="([^"]+)"', svg_data)
    circles = re.findall(r'<circle\s+cx="([^"]+)"\s+cy="([^"]+)"\s+r="([^"]+)"', svg_data)

    def rgb(c):
        if not is_valid_hex(c):
            c = "#FFFFFF"
        r, g, b = hex_to_rgb(c)
        return f"rgb({r},{g},{b})"

    rebuilt = f'<svg xmlns="http://www.w3.org/2000/svg" height="{size}" viewBox="0 0 24 24" width="{size}">'
    rebuilt += f'<path d="{paths[0]}" fill="none"/>'
    rebuilt += f'<path d="{paths[1]}" fill="{rgb(lens_color)}"/>'
    for i, (cx, cy, r) in enumerate(circles):
        color = circle_colors[i % len(circle_colors)]
        rebuilt += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{rgb(color)}"/>'
    rebuilt += '</svg>'

    png_data = cairosvg.svg2png(bytestring=rebuilt.encode("utf-8"),
                                 output_width=size, output_height=size)
    return Image.open(io.BytesIO(png_data)).convert("RGBA")


def generate_icon(theme_name):
    gth_path = None
    theme_dir = os.path.join(THEMES_DIR, theme_name)
    for f in os.listdir(theme_dir):
        if f.endswith(".gth"):
            gth_path = os.path.join(theme_dir, f)
            break
    if not gth_path:
        print(f"  [SKIP] No .gth file for {theme_name}")
        return

    with open(gth_path, "r") as f:
        data = json.load(f)

    mat = data.get("material3", {})
    primary = get_color(data, "material3", "primary", "#45d6ff")
    primary_container = get_color(data, "material3", "primaryContainer", "#1f6073")
    secondary = get_color(data, "material3", "secondary", "#86e4ff")
    tertiary = get_color(data, "material3", "tertiary", "#99768c")
    on_secondary_fixed = get_color(data, "material3", "onSecondaryFixed", "#365b66")
    surface = get_color(data, "material3", "surface", "#101014")
    surface_dim = get_color(data, "material3", "surfaceDim", "#0e0e12")
    surface_container_low = get_color(data, "material3", "surfaceContainerLow", "#1a1a1d")
    on_primary_container = get_color(data, "material3", "onPrimaryContainer", "#bef1ff")
    on_secondary_container = get_color(data, "material3", "onSecondaryContainer", "#d5f6ff")

    gradient = make_gradient(ICON_SIZE, ICON_SIZE, [surface_dim, surface, surface_container_low, primary_container])

    if os.path.exists(BG_PATH):
        bg = Image.open(BG_PATH).convert("RGBA").resize((ICON_SIZE, ICON_SIZE), Image.LANCZOS)
        gradient_rgba = gradient.convert("RGBA")
        gradient_rgba.putalpha(bg.split()[3])
        gradient = gradient_rgba

    lens_color = on_primary_container
    circle_colors = [primary, secondary, tertiary, on_secondary_container]

    svg_icon = render_multicolor_svg(SVG_PATH, ICON_SIZE, lens_color, circle_colors)

    canvas = gradient.convert("RGBA")
    icon_w, icon_h = svg_icon.size
    offset_x = (ICON_SIZE - icon_w) // 2
    offset_y = (ICON_SIZE - icon_h) // 2
    canvas.paste(svg_icon, (offset_x, offset_y), svg_icon)

    result = apply_rounded_corners(canvas, CORNER_RADIUS)

    out_path = os.path.join(theme_dir, "icon.png")
    result.save(out_path, "PNG")
    print(f"  [OK] {out_path}")


def main():
    import sys
    targets = sys.argv[1:] if len(sys.argv) > 1 else None

    if targets:
        for t in targets:
            icon_file = os.path.join(THEMES_DIR, t, "icon.png")
            if os.path.exists(icon_file):
                print(f"  [SKIP] {t} has icon.png")
                continue
            print(f"Generating: {t}")
            generate_icon(t)
    else:
        with open(os.path.join(THEMES_DIR, "theme.json"), "r") as f:
            themes = json.load(f)
        for theme in themes:
            name = theme["name"]
            icon_file = os.path.join(THEMES_DIR, name, "icon.png")
            if os.path.exists(icon_file):
                print(f"  [SKIP] {name} has icon.png")
                continue
            print(f"Generating: {name}")
            generate_icon(name)


if __name__ == "__main__":
    main()
