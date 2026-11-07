# ============================================================================
# utils.py — Module utilitaire
# Contient les constantes de style (couleurs, police), la clé de produit,
# et les fonctions partagées entre les différentes pages de l'application.
# ============================================================================

import re
import string
import customtkinter as ctk

# ─── Palette de couleurs de l'interface ──────────────────────────────
SIDEBAR_BG = "#0B1A3B"         # Fond de la barre latérale (bleu très foncé)
SIDEBAR_HOVER = "#162D5A"      # Couleur au survol d'un bouton de la sidebar
SIDEBAR_ACTIVE = "#1E3F7A"     # Couleur du bouton actif dans la sidebar
HEADER_BG = "#0F2347"          # Fond de l'en-tête principal
MAIN_BG = "#F0F4F8"            # Fond de la zone de contenu
CARD_BG = "#FFFFFF"            # Fond des cartes (composants encadrés)
ACCENT = "#1A5BC6"             # Couleur d'accentuation principale (bleu)
ACCENT_LIGHT = "#E8F0FE"       # Couleur d'accentuation claire (fond résultat)
SUCCESS = "#28A745"            # Vert — succès / poids normal
WARNING = "#FFC107"            # Jaune — avertissement / surpoids
DANGER = "#DC3545"             # Rouge — erreur / obésité
TEXT_DARK = "#1A1A2E"          # Couleur du texte principal
TEXT_MUTED = "#6B7280"         # Couleur du texte secondaire (grisé)
FONT_FAMILY = "Segoe UI"      # Police utilisée dans toute l'application

# ─── Clé d'activation du produit ─────────────────────────────────────
PRODUCT_KEY = "ANALYSE-PRO-2024-PYTHON-LIC3"

# ─── Couleurs pour les graphiques (10 couleurs distinctes) ───────────
CHART_COLORS = [
    "#1A5BC6", "#F97316", "#22C55E", "#A855F7", "#06B6D4",
    "#EF4444", "#F59E0B", "#EC4899", "#6366F1", "#14B8A6",
]


def extract_words(text):
    """
    Extrait les mots d'un texte dont la longueur dépasse 4 lettres.

    Étapes :
    1. Conversion du texte en minuscules
    2. Suppression de la ponctuation
    3. Extraction des mots (lettres latines + accents français)
    4. Filtrage : seuls les mots de plus de 4 caractères sont conservés

    Paramètre :
        text (str) : Le texte à analyser

    Retourne :
        list[str] : Liste des mots de plus de 4 lettres en minuscules
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = re.findall(r"[a-zàâäéèêëïîôùûüÿçœæ]+", text)
    return [w for w in words if len(w) > 4]


def card(parent, **kwargs):
    """
    Crée un composant 'carte' réutilisable (cadre blanc arrondi avec bordure).
    Utilisé comme conteneur visuel dans toutes les pages de l'application.

    Paramètre :
        parent : Widget parent dans lequel la carte est placée

    Retourne :
        CTkFrame : Le cadre stylisé prêt à être utilisé
    """
    return ctk.CTkFrame(
        parent, fg_color=CARD_BG, corner_radius=12,
        border_width=1, border_color="#E2E8F0", **kwargs,
    )


def section_title(parent, icon, text):
    """
    Crée un titre de section avec un icône et un texte en gras.
    Exemple d'affichage : "⚖️  Calcul de l'IMC"

    Paramètres :
        parent : Widget parent
        icon (str) : Emoji ou icône à afficher
        text (str) : Texte du titre

    Retourne :
        CTkFrame : Le cadre contenant le titre
    """
    frame = ctk.CTkFrame(parent, fg_color="transparent")
    ctk.CTkLabel(
        frame, text=f"{icon}  {text}",
        font=ctk.CTkFont(family=FONT_FAMILY, size=16, weight="bold"),
        text_color=TEXT_DARK,
    ).pack(anchor="w")
    return frame
