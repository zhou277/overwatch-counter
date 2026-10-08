from pathlib import Path
import io
import json
import urllib.request
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "map_assets.json"

def download(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 OverwatchCounterMapAssetBuilder/1.0",
            "Referer": "https://overwatch.statbanana.com/images",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def add_attribution(data: bytes, label: str) -> Image.Image:
    img = Image.open(io.BytesIO(data)).convert("RGBA")

    # Normalize to a practical size while retaining map detail.
    max_side = 1400
    scale = min(1.0, max_side / max(img.width, img.height))
    if scale < 1.0:
        img = img.resize(
            (max(1, round(img.width * scale)), max(1, round(img.height * scale))),
            Image.Resampling.LANCZOS,
        )

    footer_h = max(32, round(img.height * 0.055))
    canvas = Image.new("RGBA", (img.width, img.height + footer_h), (12, 18, 28, 255))
    canvas.paste(img, (0, 0))

    draw = ImageDraw.Draw(canvas)
    text = f"Overhead map courtesy of StatBanana / Coggle · {label}"
    font = ImageFont.load_default()

    # Dark footer + light text makes the derived copy visibly modified
    # without obscuring the tactical map.
    draw.rectangle((0, img.height, img.width, img.height + footer_h), fill=(12,18,28,255))
    draw.text((10, img.height + max(7, footer_h // 3)), text, fill=(220,230,242,255), font=font)
    return canvas

def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    successes = 0
    failures = []

    for entry in manifest["maps"]:
        target = ROOT / entry["output"]
        target.parent.mkdir(parents=True, exist_ok=True)

        try:
            raw = download(entry["url"])
            image = add_attribution(raw, entry["name"])
            image.save(target, format="PNG", optimize=True)
            print(f"[OK] {entry['name']} -> {target.relative_to(ROOT)}")
            successes += 1
        except Exception as exc:
            print(f"[FAIL] {entry['name']}: {exc}")
            failures.append(entry["name"])

    print(f"Prepared {successes}/{len(manifest['maps'])} actual overhead assets.")
    if failures:
        print("Failed maps:", ", ".join(failures))

if __name__ == "__main__":
    main()
