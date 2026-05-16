from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "demo_frames"
WIDTH = 1280
HEIGHT = 720
FPS = 12
DURATION = 14
TOTAL_FRAMES = FPS * DURATION

BG = "#070b14"
PANEL = "#0f1625"
PANEL_2 = "#121c31"
BORDER = "#233252"
TEXT = "#e6edf7"
MUTED = "#8da2c7"
ACCENT = "#62d0ff"
GREEN = "#7ee787"
RED = "#ff6b7a"
YELLOW = "#ffd866"


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def ease(t: float) -> float:
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))


def load_font(size: int, mono: bool = False) -> ImageFont.FreeTypeFont:
    if mono:
        return ImageFont.truetype("C:/Windows/Fonts/consola.ttf", size=size)
    return ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", size=size)


FONT_UI_18 = load_font(18)
FONT_UI_22 = load_font(22)
FONT_UI_28 = load_font(28)
FONT_UI_34 = load_font(34)
FONT_MONO_20 = load_font(20, mono=True)
FONT_MONO_22 = load_font(22, mono=True)


CODE_LINES = [
    "export function pickProfile(config: Config, env: RuntimeEnv) {",
    "  const primary = config.profile?.trim();",
    "  const fallback = env.DEFAULT_PROFILE?.trim();",
    "",
    "  if (!primary) return fallback || \"guest\";",
    "  if (!fallback) return primary;",
    "",
    "  return fallback;",
    "}",
]

FIXED_LINES = [
    "export function pickProfile(config: Config, env: RuntimeEnv) {",
    "  const primary = config.profile?.trim();",
    "  const fallback = env.DEFAULT_PROFILE?.trim();",
    "",
    "  if (!primary) return fallback || \"guest\";",
    "  if (!fallback) return primary;",
    "",
    "  return primary;",
    "}",
]

TERMINAL_FAIL = [
    "> npm test -- pickProfile.test.ts",
    "",
    " FAIL  pickProfile.test.ts",
    "  pickProfile",
    "    x keeps explicit profile over fallback",
    "",
    " Expected: \"pro\"",
    " Received: \"guest\"",
]

TERMINAL_PASS = [
    "> npm test -- pickProfile.test.ts",
    "",
    " PASS  pickProfile.test.ts",
    "  pickProfile",
    "    √ keeps explicit profile over fallback",
    "",
    " Tests: 1 passed",
    " Time: 0.79s",
]


def draw_panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, subtitle: str) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=24, fill=PANEL, outline=BORDER, width=2)
    draw.text((x1 + 24, y1 + 18), title, font=FONT_UI_28, fill=TEXT)
    draw.text((x1 + 24, y1 + 54), subtitle, font=FONT_UI_18, fill=MUTED)


def draw_badge(draw: ImageDraw.ImageDraw, pos: tuple[int, int], text: str, fill: str) -> None:
    x, y = pos
    w = 18 * len(text) + 36
    h = 44
    draw.rounded_rectangle((x, y, x + w, y + h), radius=16, fill=fill)
    draw.text((x + 18, y + 10), text, font=FONT_UI_22, fill="#061019")


def draw_code(draw: ImageDraw.ImageDraw, lines: list[str], typed_line: int | None = None, typed_chars: int = 0) -> None:
    x = 80
    y = 236
    line_h = 42
    for idx, line in enumerate(lines, start=1):
        num_y = y + (idx - 1) * line_h
        draw.text((92, num_y), f"{idx}", font=FONT_MONO_20, fill="#516485")
        color = TEXT
        if idx == 8:
            color = RED if lines[idx - 1].strip() == "return fallback;" else GREEN
        visible = line
        if typed_line == idx:
            visible = line[:typed_chars]
        draw.text((138, num_y), visible, font=FONT_MONO_22, fill=color)


def draw_terminal(draw: ImageDraw.ImageDraw, lines: list[str], y_shift: int = 0) -> None:
    base_x = 760
    base_y = 236 + y_shift
    line_h = 34
    for idx, line in enumerate(lines):
        fill = TEXT
        if "FAIL" in line or "Received" in line or "x keeps" in line:
            fill = RED
        elif "PASS" in line or "√ keeps" in line or "passed" in line:
            fill = GREEN
        elif line.startswith("> "):
            fill = ACCENT
        draw.text((base_x, base_y + idx * line_h), line, font=FONT_MONO_20, fill=fill)


def draw_overlay(draw: ImageDraw.ImageDraw, frame: int) -> None:
    if frame < 24:
        prompt = "Use $safe-code-agent for this."
        draw.rounded_rectangle((866, 48, 1224, 94), radius=16, fill=PANEL_2, outline="#2a4b68")
        draw.text((886, 60), prompt, font=FONT_UI_18, fill=TEXT)
        return
    if frame < 72:
        points = ["Inspect caller/fallback path", "Simulate failing branch", "Patch only one line"]
        draw.rounded_rectangle((812, 468, 1200, 638), radius=20, fill=PANEL_2, outline="#2e466e")
        draw.text((836, 490), "Safe Code Agent", font=FONT_UI_22, fill=GREEN)
        for i, point in enumerate(points):
            draw.text((842, 530 + i * 30), f"- {point}", font=FONT_UI_18, fill=TEXT)
        return
    draw.rounded_rectangle((780, 530, 1190, 632), radius=20, fill=PANEL_2, outline="#2e466e")
    draw.text((806, 554), "Verify honestly", font=FONT_UI_28, fill=ACCENT)
    draw.text((808, 596), "Run: npm test -- pickProfile.test.ts", font=FONT_UI_18, fill=TEXT)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in OUT_DIR.glob("frame-*.png"):
        path.unlink()

    for frame in range(TOTAL_FRAMES):
        t = frame / FPS
        img = Image.new("RGB", (WIDTH, HEIGHT), BG)
        draw = ImageDraw.Draw(img)

        draw.rounded_rectangle((32, 32, WIDTH - 32, HEIGHT - 32), radius=28, outline="#18243d", width=2)
        draw.text((64, 54), "safe-code-agent demo", font=FONT_UI_34, fill=TEXT)
        draw.text((64, 98), "AI inspects, finds the fallback bug, patches one line, then verifies", font=FONT_UI_18, fill=MUTED)

        draw_panel(draw, (56, 136, 728, 652), "src/pickProfile.ts", "Buggy fallback logic")
        draw_panel(draw, (748, 136, 1224, 652), "terminal", "Fail first, then verify")

        if t < 6:
            code = CODE_LINES
            terminal = TERMINAL_FAIL
        elif t < 10:
            code = FIXED_LINES
            terminal = TERMINAL_FAIL
        else:
            code = FIXED_LINES
            terminal = TERMINAL_PASS

        typed_line = None
        typed_chars = 0
        if 6 <= t < 9.2:
            typed_line = 8
            progress = ease((t - 6) / 3.2)
            target = FIXED_LINES[7]
            typed_chars = max(1, int(len(target) * progress))
            code = FIXED_LINES.copy()
        draw_code(draw, code, typed_line=typed_line, typed_chars=typed_chars)

        terminal_shift = 0
        if 10 <= t < 12:
            terminal_shift = int(lerp(8, 0, ease((t - 10) / 2)))
        draw_terminal(draw, terminal, y_shift=terminal_shift)

        if 2 <= t < 6:
            pulse = 2 + int(3 * ease((t - 2) / 4))
            top = 236 + 7 * 42 - 4
            draw.rounded_rectangle((130, top - 4, 500, top + 34), radius=12, outline=RED, width=pulse)
            draw.text((514, top - 2), "Fallback overrides explicit choice", font=FONT_UI_18, fill=RED)
        elif 6 <= t < 9.5:
            top = 236 + 7 * 42 - 4
            draw.rounded_rectangle((130, top - 4, 414, top + 34), radius=12, outline=GREEN, width=3)
            draw.text((428, top - 2), "One-line fix", font=FONT_UI_18, fill=GREEN)

        if t >= 10:
            draw_badge(draw, (922, 146), "test passed", "#143622")
        else:
            draw_badge(draw, (932, 146), "test failing", "#3a1520")

        draw_overlay(draw, frame)
        img.save(OUT_DIR / f"frame-{frame:04d}.png")


if __name__ == "__main__":
    main()
