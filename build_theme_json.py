#!/usr/bin/env python3
"""بر اساس نام هر تم (پوشه)، داده‌های آن را می‌خواند و در theme.json ذخیره می‌کند."""

import os
import re
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
THEME_JSON = os.path.join(BASE_DIR, "theme.json")

REPO_OWNER = "HanzoDev1375"
REPO_NAME = "ghostidetheme"
REPO_BRANCH = "main"

ICON_NAME = "icon.png"

WALLPAPER_NAMES = [
    "wallpaper.png",
    "wallpaper.jpg",
    "backgeound.png",
    "background.png",
    "backgeound.jpg",
]


def find_icon(folder_path):
    """فایل icon.png را داخل پوشه پیدا می‌کند."""
    path = os.path.join(folder_path, ICON_NAME)
    if os.path.isfile(path):
        return ICON_NAME
    return ""


def find_wallpaper(folder_path):
    """تصویر پس‌زمینه (wallpaper) را داخل پوشه پیدا می‌کند."""
    for name in WALLPAPER_NAMES:
        path = os.path.join(folder_path, name)
        if os.path.isfile(path):
            return name
    for fname in sorted(os.listdir(folder_path)):
        if fname.lower().startswith("wallpaper") or fname.lower().startswith(
            "backgeound"
        ):
            return fname
    return ""


def find_gth(folder_path):
    """نام فایل .gth را در پوشه پیدا می‌کند."""
    for fname in sorted(os.listdir(folder_path)):
        if fname.lower().endswith(".gth"):
            path = os.path.join(folder_path, fname)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    f.read()
                return fname
            except (UnicodeDecodeError, OSError):
                continue
    return ""


def find_doc(folder_path):
    """فایل .md (سند/توضیحات تم) را در پوشه پیدا می‌کند."""
    for fname in sorted(os.listdir(folder_path)):
        if fname.lower().endswith(".md"):
            return fname
    return ""


def gth_download_link(gth_name):
    """لینک مستقیم دانلود فایل .gth را می‌سازد."""
    return f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{REPO_BRANCH}/{gth_name}"


def autoversion(current):
    """شماره نسخه را در صورت تغییر افزایش می‌دهد."""
    try:
        return int(current) + 1
    except (TypeError, ValueError):
        return 1


def existing_entries():
    """تعداد ورودی‌های قبلی را برای ساخت نسخه جدید می‌خواند."""
    try:
        with open(THEME_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def main():
    entries = existing_entries()

    # برای افزایش نسخه، نام تم‌های قبلی را نگه می‌داریم
    previous = {e.get("name"): e for e in entries if isinstance(e, dict)}

    result = []

    for folder in sorted(os.listdir(BASE_DIR)):
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.isdir(folder_path) or folder in (".git",):
            continue

        wallpaper = find_wallpaper(folder_path)
        icon_name = find_icon(folder_path)
        gth_name = find_gth(folder_path)
        doc_name = find_doc(folder_path)

        old = previous.get(folder, {})
        version = autoversion(old.get("version", 0))

        entry = {
            "name": folder,
            "icon": gth_download_link(os.path.join(folder, icon_name))
            if icon_name
            else gth_download_link(os.path.join(folder, wallpaper))
            if wallpaper
            else "",
            "doc": gth_download_link(os.path.join(folder, doc_name))
            if doc_name
            else "",
            "version": version,
            "devname": "ghost",
            "linkdownload": gth_download_link(os.path.join(folder, gth_name))
            if gth_name
            else "",
        }
        result.append(entry)

    with open(THEME_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✓ {len(result)} تم در {THEME_JSON} ذخیره شد:")
    for e in result:
        print(f"  - {e['name']}  (version {e['version']})")


if __name__ == "__main__":
    main()