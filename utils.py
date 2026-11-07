import re
import string
import customtkinter as ctk

# ─── Couleurs & style ────────────────────────────────────────────────
SIDEBAR_BG = "#0B1A3B"
SIDEBAR_HOVER = "#162D5A"
SIDEBAR_ACTIVE = "#1E3F7A"
HEADER_BG = "#0F2347"
MAIN_BG = "#F0F4F8"
CARD_BG = "#FFFFFF"
ACCENT = "#1A5BC6"
ACCENT_LIGHT = "#E8F0FE"
SUCCESS = "#28A745"
WARNING = "#FFC107"
DANGER = "#DC3545"
TEXT_DARK = "#1A1A2E"
TEXT_MUTED = "#6B7280"
FONT_FAMILY = "Segoe UI"

PRODUCT_KEY = "ANALYSE-PRO-2024-PYTHON-LIC3"

CHART_COLORS = [
    "#1A5BC6", "#F97316", "#22C55E", "#A855F7", "#06B6D4",
    "#EF4444", "#F59E0B", "#EC4899", "#6366F1", "#14B8A6",
]


def extract_words(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = re.findall(r"[a-zàâäéèêëïîôùûüÿçœæ]+", text)
    return [w for w in words if len(w) > 4]


def card(parent, **kwargs):
    return ctk.CTkFrame(
        parent, fg_color=CARD_BG, corner_radius=12,
        border_width=1, border_color="#E2E8F0", **kwargs,
    )


def section_title(parent, icon, text):
    frame = ctk.CTkFrame(parent, fg_color="transparent")
    ctk.CTkLabel(
        frame, text=f"{icon}  {text}",
        font=ctk.CTkFont(family=FONT_FAMILY, size=16, weight="bold"),
        text_color=TEXT_DARK,
    ).pack(anchor="w")
    return frame
