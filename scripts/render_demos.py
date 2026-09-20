from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg


ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "public" / "images"
OUTPUT = ROOT / "public" / "demos"
FRAMES = ROOT / ".render-frames"
W, H = 1920, 1080


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


SANS = r"C:\Windows\Fonts\segoeui.ttf"
SANS_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
MONO = r"C:\Windows\Fonts\consola.ttf"
MONO_BOLD = r"C:\Windows\Fonts\consolab.ttf"


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, size: int,
         fill: str, *, bold: bool = False, mono: bool = False, anchor: str | None = None) -> None:
    path = MONO_BOLD if mono and bold else MONO if mono else SANS_BOLD if bold else SANS
    draw.text(xy, value, font=font(path, size), fill=fill, anchor=anchor)


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str,
            outline: str | None = None, radius: int = 24, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def cover(source: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    if len(box) == 2:
        w, h = box
    else:
        _, _, w, h = box
    ratio = max(w / source.width, h / source.height)
    resized = source.resize((round(source.width * ratio), round(source.height * ratio)), Image.Resampling.LANCZOS)
    left = (resized.width - w) // 2
    top = (resized.height - h) // 2
    return resized.crop((left, top, left + w, top + h))


def contain(source: Image.Image, box: tuple[int, int, int, int], background: str = "#0b1625") -> Image.Image:
    if len(box) == 2:
        w, h = box
    else:
        _, _, w, h = box
    ratio = min(w / source.width, h / source.height)
    resized = source.resize((round(source.width * ratio), round(source.height * ratio)), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (w, h), background)
    canvas.paste(resized, ((w - resized.width) // 2, (h - resized.height) // 2))
    return canvas


def chrome() -> Image.Image:
    return Image.new("RGB", (W, H), "#07111e")


def grid(draw: ImageDraw.ImageDraw) -> None:
    for x in range(0, W, 96):
        draw.line((x, 0, x, H), fill="#0b1b2b", width=1)
    for y in range(0, H, 96):
        draw.line((0, y, W, y), fill="#0b1b2b", width=1)


def image_panel(canvas: Image.Image, source: Image.Image, box: tuple[int, int, int, int], *, contain_mode: bool = False) -> None:
    x, y, w, h = box
    panel = contain(source, (w - 16, h - 16)) if contain_mode else cover(source, (w - 16, h - 16))
    rounded(ImageDraw.Draw(canvas), (x, y, x + w, y + h), "#0f2034", outline="#28415d", radius=30, width=2)
    canvas.paste(panel, (x + 8, y + 8))


def title_slide(product: str, subtitle: str, accent: str, eyebrow: str) -> Image.Image:
    canvas = chrome()
    draw = ImageDraw.Draw(canvas)
    grid(draw)
    draw.ellipse((1450, -250, 2080, 380), fill=accent)
    draw.ellipse((1610, -95, 1940, 235), fill="#07111e")
    text(draw, (150, 205), eyebrow.upper(), 24, accent, bold=True, mono=True)
    text(draw, (145, 320), product, 112, "#f3f7fb", bold=True)
    text(draw, (152, 465), subtitle, 38, "#9eb4ca")
    draw.line((152, 610, 630, 610), fill=accent, width=5)
    text(draw, (152, 665), "HENRY WILLIAMS  /  SELECTED WORK", 22, "#6f8ba5", bold=True, mono=True)
    text(draw, (150, 965), "PUBLIC DEMO  ·  EVIDENCE-LED  ·  NO PRIVATE DATA", 18, "#607b94", mono=True)
    return canvas


def product_slide(product: str, kicker: str, headline: str, bullets: list[str],
                  source: Image.Image, accent: str, *, contain_mode: bool = False) -> Image.Image:
    canvas = chrome()
    draw = ImageDraw.Draw(canvas)
    text(draw, (105, 74), product.upper(), 18, accent, bold=True, mono=True)
    text(draw, (105, 124), kicker, 20, "#6f8ba5", mono=True)
    text(draw, (105, 190), headline, 43, "#f3f7fb", bold=True)
    image_panel(canvas, source, (105, 300, 1190, 650), contain_mode=contain_mode)
    text(draw, (1375, 330), "PROOF", 18, accent, bold=True, mono=True)
    y = 405
    for bullet in bullets:
        draw.ellipse((1375, y + 9, 1387, y + 21), fill=accent)
        text(draw, (1410, y), bullet, 25, "#dce7f1", bold=True)
        y += 82
    draw.line((1375, 760, 1780, 760), fill="#28415d", width=2)
    text(draw, (1375, 810), "synthetic / public demo surface", 18, "#6f8ba5", mono=True)
    return canvas


def metric_slide(product: str, accent: str, left_label: str, left_value: str,
                 right_label: str, right_value: str, note: str) -> Image.Image:
    canvas = chrome()
    draw = ImageDraw.Draw(canvas)
    grid(draw)
    text(draw, (150, 120), product.upper(), 18, accent, bold=True, mono=True)
    text(draw, (150, 190), "Make the important failure visible.", 56, "#f3f7fb", bold=True)
    rounded(draw, (150, 360, 840, 720), "#0f2034", outline="#28415d", radius=26, width=2)
    rounded(draw, (1080, 360, 1770, 720), "#0f2034", outline=accent, radius=26, width=2)
    text(draw, (205, 435), left_label.upper(), 18, "#6f8ba5", bold=True, mono=True)
    text(draw, (205, 510), left_value, 64, "#f3f7fb", bold=True)
    text(draw, (1135, 435), right_label.upper(), 18, accent, bold=True, mono=True)
    text(draw, (1135, 510), right_value, 64, accent, bold=True)
    text(draw, (150, 845), note, 28, "#9eb4ca")
    return canvas


def end_slide(product: str, line: str, accent: str, repo: str) -> Image.Image:
    canvas = chrome()
    draw = ImageDraw.Draw(canvas)
    grid(draw)
    text(draw, (150, 215), product, 78, "#f3f7fb", bold=True)
    text(draw, (153, 345), line, 34, "#9eb4ca")
    rounded(draw, (150, 500, 1770, 680), "#0f2034", outline="#28415d", radius=24, width=2)
    text(draw, (205, 566), repo, 28, accent, bold=True, mono=True)
    text(draw, (150, 910), "github.com/ANKOHR  ·  live dashboard  ·  evidence record", 20, "#6f8ba5", mono=True)
    return canvas


def render(name: str, slides: list[tuple[Image.Image, float]]) -> None:
    FRAMES.mkdir(exist_ok=True)
    frame_paths: list[Path] = []
    for index, (slide, _) in enumerate(slides):
        path = FRAMES / f"{name}-{index:02d}.png"
        slide.save(path, optimize=True)
        frame_paths.append(path)

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    inputs: list[str] = [ffmpeg, "-y", "-hide_banner"]
    for path, duration in slides_to_paths(slides, frame_paths):
        inputs += ["-loop", "1", "-t", str(duration), "-i", str(path)]
    concat_inputs = "".join(f"[{i}:v]" for i in range(len(slides)))
    filter_graph = f"{concat_inputs}concat=n={len(slides)}:v=1:a=0[v]"
    output = OUTPUT / f"{name}.mp4"
    inputs += ["-filter_complex", filter_graph, "-map", "[v]", "-r", "24", "-c:v", "libx264", "-preset", "medium", "-crf", "22", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output)]
    subprocess.run(inputs, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(output)


def slides_to_paths(slides: list[tuple[Image.Image, float]], paths: list[Path]):
    for (_, duration), path in zip(slides, paths, strict=True):
        yield path, duration


def main() -> None:
    opspilot_dashboard = Image.open(IMAGES / "opspilot-dashboard.png").convert("RGB")
    opspilot_approval = Image.open(IMAGES / "opspilot-approval.png").convert("RGB")
    opspilot_trace = Image.open(IMAGES / "opspilot-run-trace.png").convert("RGB")
    verity_case = Image.open(IMAGES / "veritydocs-case.png").convert("RGB")
    verity_evidence = Image.open(IMAGES / "veritydocs-evidence.png").convert("RGB")
    verity_review = Image.open(IMAGES / "veritydocs-fin001-review.png").convert("RGB")

    render("opspilot", [
        (title_slide("OpsPilot", "Auditable workflow automation with human approval", "#62a5ff", "flagship system"), 4),
        (product_slide("OpsPilot", "01  /  OPERATIONS OVERVIEW", "Events become typed, observable work.", ["workflow metrics", "sandbox-safe defaults", "approval-aware runs"], opspilot_dashboard, "#62a5ff"), 12),
        (product_slide("OpsPilot", "02  /  HUMAN CONTROL", "External actions pause for a decision.", ["approval inbox", "proposed response", "approve or reject"], opspilot_approval, "#f5b84b"), 14),
        (product_slide("OpsPilot", "03  /  EXECUTION TRACE", "Every step leaves an inspectable record.", ["typed outputs", "tool latency + cost", "replayable checkpoint"], opspilot_trace, "#8b7cff"), 16),
        (metric_slide("OpsPilot", "#62a5ff", "verified locally", "60 backend tests", "live lane", "Gmail OAuth", "The deployed Gmail path is separately evidenced; provider acceptance is not recipient delivery."), 14),
        (end_slide("OpsPilot", "Reliable AI operations, with a human in the loop.", "#62a5ff", "github.com/ANKOHR/opspilot"), 15),
    ])

    render("veritydocs", [
        (title_slide("VerityDocs", "Evidence-backed document intelligence", "#f0b45b", "flagship data system"), 4),
        (product_slide("VerityDocs", "01  /  CASE WORKSPACE", "Messy source files become reviewable facts.", ["PDF + spreadsheet inputs", "reconciliation context", "exceptions stay visible"], verity_case, "#f0b45b"), 12),
        (product_slide("VerityDocs", "02  /  PROVENANCE", "Click a value. See where it came from.", ["Tesseract OCR", "page-level evidence", "bounding-box source link"], verity_evidence, "#62c6a5", contain_mode=True), 14),
        (product_slide("VerityDocs", "03  /  SAFE FAILURE", "A wrong total becomes a review item.", ["gross: £9,900", "expected: £9,600", "FIN-001: FAIL"], verity_review, "#f06f66"), 15),
        (metric_slide("VerityDocs", "#f0b45b", "deterministic check", "£8,000 + £1,600", "validation", "£9,600  /  PASS", "The deliberate £9,900 fixture fails closed and routes to human review. Synthetic documents only."), 15),
        (end_slide("VerityDocs", "Trust the extraction because the evidence stays attached.", "#f0b45b", "github.com/ANKOHR/veritydocs"), 15),
    ])


if __name__ == "__main__":
    main()
