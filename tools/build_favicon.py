"""Build icons/favicon.ico (16, 32 and 48 px) from the PNGs made by tools/render-icons.html.

Run from the project folder:  python3 tools/build_favicon.py   (needs Pillow)
"""
import os
from PIL import Image

icons = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "icons")
big = Image.open(os.path.join(icons, "icon-48.png")).convert("RGBA")
big.save(os.path.join(icons, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
print("icons/favicon.ico")
