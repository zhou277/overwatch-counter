from pathlib import Path
import io
import json
import re
import urllib.request
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "map_assets.json"

def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 OverwatchCounterMapAssetBuilder/2.0",
            "Referer": "https://overwatch.statbanana.com/images",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def download_from_google_drive(file_id: str) -> bytes:
    primary = f"https://drive.usercontent.google.com/download?id={file_id}&export=download&confirm=t"
    data = fetch_bytes(primary)
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return data

    fallback = f"https://drive.google.com/uc?export=download&id={file_id}"
    data = fetch_bytes(fallback)
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return data

    text = data.decode("utf-8", errors="ignore")
    m = re.search(r'confirm=([0-9A-Za-z_]+)', text)
    if m:
        url = f"https://drive.google.com/uc?export=download&confirm={m.group(1)}&id={file_id}"
        data = fetch_bytes(url)
        if data[:8] == b"\x89PNG\r\n\x1a\n":
            return data

    raise RuntimeError("Google Drive did not return a PNG")

def add_corner_attribution(data: bytes) -> Image.Image:
    img = Image.open(io.BytesIO(data)).convert("RGBA")
    draw = ImageDraw.Draw(img)
    text = "StatBanana / Coggle"
    font = ImageFont.load_default()

    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
    except Exception:
        tw, th = 90, 12

    pad = max(6, img.width // 400)
    rect_w = tw + pad * 2
    rect_h = th + pad * 2
    x0 = img.width - rect_w - pad
    y0 = img.height - rect_h - pad

    draw.rounded_rectangle((x0, y0, x0 + rect_w, y0 + rect_h), radius=pad, fill=(12,18,28,165))
    draw.text((x0 + pad, y0 + pad - 1), text, fill=(235,242,250,235), font=font)
    return img

def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    successes, failures = 0, []
    for entry in manifest["maps"]:
        target = ROOT / entry["output"]
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            raw = download_from_google_drive(entry.get("drive_file_id",""))
            img = add_corner_attribution(raw)
            img.save(target, format="PNG", optimize=True)
            print(f"[OK] {entry['name']} {entry.get('resolution','')} -> {target.relative_to(ROOT)}")
            successes += 1
        except Exception as exc:
            try:
                raw = fetch_bytes(entry["fallback_preview"])
                img = add_corner_attribution(raw)
                img.save(target, format="PNG", optimize=True)
                print(f"[FALLBACK] {entry['name']} preview used -> {target.relative_to(ROOT)}")
                successes += 1
            except Exception as exc2:
                print(f"[FAIL] {entry['name']}: {exc} / preview failed: {exc2}")
                failures.append(entry["name"])

    print(f"Prepared {successes}/{len(manifest['maps'])} local overhead assets.")
    if failures:
        print("Failed maps:", ", ".join(failures))

if __name__ == "__main__":
    main()
