# ============================================================================
# accueil.py — Page d'accueil (Dashboard)
# Affiche un message de bienvenue et des cartes de navigation rapide
# vers les différentes fonctionnalités de l'application.
# ============================================================================

import customtkinter as ctk
from utils import (
    FONT_FAMILY, ACCENT, SIDEBAR_ACTIVE, TEXT_DARK, TEXT_MUTED, card,
)


class PageAccueil(ctk.CTkScrollableFrame):
    """
    Page d'accueil de l'application.
    Présente un dashboard avec des cartes cliquables pour accéder
    rapidement aux fonctionnalités : IMC, Analyse Texte, Analyse PDF,
    Graphiques et Activation.
    """

    def __init__(self, parent, navigate_callback):
        """
        Paramètres :
            parent : Widget parent (zone de contenu)
            navigate_callback : Fonction de navigation pour changer de page
        """
        super().__init__(parent, fg_color="transparent")
        self.navigate = navigate_callback
        self._build()

    def _build(self):
        """Construit l'interface de la page d'accueil."""

        # ── Carte de bienvenue ──
        welcome = card(self)
        welcome.pack(fill="x", pady=(0, 15))
        ctk.CTkLabel(
            welcome, text="🎉  Bienvenue dans Analyse Pro Python !",
            font=ctk.CTkFont(family=FONT_FAMILY, size=20, weight="bold"),
            text_color=ACCENT,
        ).pack(padx=25, pady=(20, 5), anchor="w")
        ctk.CTkLabel(
            welcome,
            text="Cette application vous permet de calculer votre IMC, analyser des textes,\n"
                 "extraire les mots les plus fréquents de fichiers PDF, et visualiser les résultats.",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13),
            text_color=TEXT_MUTED, justify="left",
        ).pack(padx=25, pady=(0, 20), anchor="w")

        # ── Grille des 3 cartes principales (IMC, Texte, PDF) ──
        cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        cards_frame.pack(fill="x", pady=(0, 15))
        cards_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Définition des fonctionnalités principales
        features = [
            ("⚖️", "Calcul IMC",
             "Calculez votre indice de\nmasse corporelle et obtenez\nune interprétation détaillée.", "imc"),
            ("📝", "Analyse Texte",
             "Collez un texte et découvrez\nles mots de plus de 4 lettres\navec leurs fréquences.", "texte"),
            ("📄", "Analyse PDF",
             "Chargez un fichier PDF et\ntrouvez les 10 mots les\nplus fréquents.", "pdf"),
        ]

        # Création dynamique des cartes de fonctionnalités
        for i, (icon, title, desc, target) in enumerate(features):
            c = card(cards_frame)
            c.grid(row=0, column=i, padx=8, sticky="nsew")
            ctk.CTkLabel(c, text=icon, font=ctk.CTkFont(size=36)).pack(pady=(20, 5))
            ctk.CTkLabel(
                c, text=title,
                font=ctk.CTkFont(family=FONT_FAMILY, size=15, weight="bold"),
                text_color=TEXT_DARK,
            ).pack(pady=(0, 5))
            ctk.CTkLabel(
                c, text=desc,
                font=ctk.CTkFont(family=FONT_FAMILY, size=12),
                text_color=TEXT_MUTED, justify="center",
            ).pack(pady=(0, 10))
            ctk.CTkButton(
                c, text="Ouvrir  →",
                font=ctk.CTkFont(family=FONT_FAMILY, size=12),
                fg_color=ACCENT, hover_color=SIDEBAR_ACTIVE,
                corner_radius=8, height=35,
                command=lambda t=target: self.navigate(t),
            ).pack(pady=(5, 20), padx=20, fill="x")

        # ── Cartes secondaires (Graphiques, Activation) ──
        extra_frame = ctk.CTkFrame(self, fg_color="transparent")
        extra_frame.pack(fill="x")
        extra_frame.grid_columnconfigure((0, 1), weight=1)

        for col, (icon, title, desc, target) in enumerate([
            ("📊", "Graphiques",
             "Visualisez la distribution des\nmots sous forme de graphiques.", "graphiques"),
            ("🔑", "Activation",
             "Activez votre produit avec\nune clé de licence.", "activation"),
        ]):
            c = card(extra_frame)
            c.grid(row=0, column=col, padx=8 if col == 0 else (8, 0), sticky="nsew")
            ctk.CTkLabel(c, text=icon, font=ctk.CTkFont(size=30)).pack(pady=(20, 5))
            ctk.CTkLabel(
                c, text=title,
                font=ctk.CTkFont(family=FONT_FAMILY, size=15, weight="bold"),
                text_color=TEXT_DARK,
            ).pack()
            ctk.CTkLabel(
                c, text=desc,
                font=ctk.CTkFont(family=FONT_FAMILY, size=12),
                text_color=TEXT_MUTED, justify="center",
            ).pack(pady=5)
            ctk.CTkButton(
                c, text="Ouvrir  →",
                font=ctk.CTkFont(family=FONT_FAMILY, size=12),
                fg_color=ACCENT, hover_color=SIDEBAR_ACTIVE,
                corner_radius=8, height=35,
                command=lambda t=target: self.navigate(t),
            ).pack(pady=(5, 20), padx=20, fill="x")
