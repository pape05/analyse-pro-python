# ============================================================================
# imc.py — Page de calcul de l'IMC (Tâche 1)
# Permet à l'utilisateur de saisir son poids et sa taille,
# puis calcule l'Indice de Masse Corporelle avec :
# - L'interprétation (maigreur, normal, surpoids, obésité)
# - Un conseil personnalisé
# - Une barre visuelle colorée avec un indicateur de position
# ============================================================================

import tkinter as tk
import customtkinter as ctk
from utils import (
    FONT_FAMILY, ACCENT, ACCENT_LIGHT, SIDEBAR_ACTIVE,
    SUCCESS, WARNING, DANGER, TEXT_DARK, TEXT_MUTED,
    card, section_title,
)


class PageIMC(ctk.CTkScrollableFrame):
    """
    Page de calcul de l'IMC.
    Formule utilisée : IMC = poids (kg) / taille (m)²
    Classification OMS :
        - < 18.5     → Maigreur
        - 18.5 – 24.9 → Poids normal
        - 25 – 29.9   → Surpoids
        - ≥ 30        → Obésité
    """

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self._build()

    def _build(self):
        """Construit le formulaire de saisie (poids, taille) et le bouton de calcul."""
        c = card(self)
        c.pack(fill="x", pady=(0, 15))

        section_title(c, "⚖️", "Calcul de l'IMC").pack(padx=25, pady=(20, 15), anchor="w")

        # ── Formulaire de saisie ──
        form = ctk.CTkFrame(c, fg_color="transparent")
        form.pack(padx=25, fill="x")

        # Champ de saisie du poids
        ctk.CTkLabel(
            form, text="Poids (kg) :",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13), text_color=TEXT_DARK,
        ).grid(row=0, column=0, sticky="w", pady=8)
        self.entry_poids = ctk.CTkEntry(
            form, width=200, height=38,
            font=ctk.CTkFont(family=FONT_FAMILY, size=13),
            placeholder_text="Ex: 70",
        )
        self.entry_poids.grid(row=0, column=1, padx=(15, 0), pady=8)

        # Champ de saisie de la taille
        ctk.CTkLabel(
            form, text="Taille (m) :",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13), text_color=TEXT_DARK,
        ).grid(row=1, column=0, sticky="w", pady=8)
        self.entry_taille = ctk.CTkEntry(
            form, width=200, height=38,
            font=ctk.CTkFont(family=FONT_FAMILY, size=13),
            placeholder_text="Ex: 1.75",
        )
        self.entry_taille.grid(row=1, column=1, padx=(15, 0), pady=8)

        # Bouton de calcul
        ctk.CTkButton(
            c, text="📐  Calculer l'IMC",
            font=ctk.CTkFont(family=FONT_FAMILY, size=14, weight="bold"),
            fg_color=ACCENT, hover_color=SIDEBAR_ACTIVE,
            corner_radius=10, height=45,
            command=self._calculer,
        ).pack(padx=25, pady=15, fill="x")

        # Zone d'affichage des résultats (remplie dynamiquement)
        self.result_frame = ctk.CTkFrame(c, fg_color="transparent")
        self.result_frame.pack(padx=25, pady=(0, 20), fill="x")

    def _calculer(self):
        """
        Calcule l'IMC à partir des valeurs saisies et affiche :
        - La valeur numérique de l'IMC
        - La catégorie (badge coloré)
        - Un conseil personnalisé
        - Une barre visuelle avec un curseur triangulaire
        """
        # Nettoyage des résultats précédents
        for w in self.result_frame.winfo_children():
            w.destroy()

        # Validation des entrées utilisateur
        try:
            poids = float(self.entry_poids.get().replace(",", "."))
            taille = float(self.entry_taille.get().replace(",", "."))
            if poids <= 0 or taille <= 0:
                raise ValueError
        except ValueError:
            ctk.CTkLabel(
                self.result_frame,
                text="❌  Veuillez entrer des valeurs numériques valides.",
                font=ctk.CTkFont(family=FONT_FAMILY, size=13), text_color=DANGER,
            ).pack(pady=10)
            return

        # Calcul de l'IMC : poids / taille²
        imc = poids / (taille ** 2)

        # Détermination de la catégorie selon la classification OMS
        if imc < 18.5:
            cat, couleur = "Maigreur", "#3B82F6"
            conseil = "Votre IMC indique une insuffisance pondérale. Consultez un professionnel de santé."
        elif imc < 25:
            cat, couleur = "Poids normal", SUCCESS
            conseil = "Votre IMC est dans la plage normale. Continuez à maintenir un mode de vie sain !"
        elif imc < 30:
            cat, couleur = "Surpoids", WARNING
            conseil = "Votre IMC indique un surpoids. Une alimentation équilibrée et de l'exercice sont recommandés."
        else:
            cat, couleur = "Obésité", DANGER
            conseil = "Votre IMC indique une obésité. Il est conseillé de consulter un professionnel de santé."

        # ── Affichage de la valeur de l'IMC ──
        result_card = ctk.CTkFrame(self.result_frame, fg_color=ACCENT_LIGHT, corner_radius=12)
        result_card.pack(fill="x", pady=(5, 10))

        top = ctk.CTkFrame(result_card, fg_color="transparent")
        top.pack(pady=(20, 10))
        ctk.CTkLabel(top, text="✅", font=ctk.CTkFont(size=28)).pack(side="left", padx=(0, 10))
        ctk.CTkLabel(
            top, text=f"IMC : {imc:.2f}",
            font=ctk.CTkFont(family=FONT_FAMILY, size=24, weight="bold"),
            text_color=TEXT_DARK,
        ).pack(side="left")

        # ── Badge coloré de la catégorie ──
        badge = ctk.CTkFrame(result_card, fg_color=couleur, corner_radius=8)
        badge.pack(pady=5)
        ctk.CTkLabel(
            badge, text=f"  {cat}  ",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13, weight="bold"),
            text_color="#FFFFFF",
        ).pack(padx=10, pady=5)

        # ── Conseil personnalisé ──
        ctk.CTkLabel(
            result_card, text=conseil,
            font=ctk.CTkFont(family=FONT_FAMILY, size=12),
            text_color=TEXT_MUTED, wraplength=500,
        ).pack(pady=(5, 15))

        # ── Barre visuelle colorée (4 segments) ──
        bar_frame = ctk.CTkFrame(self.result_frame, fg_color="#FFFFFF", corner_radius=10)
        bar_frame.pack(fill="x", pady=5)

        canvas = tk.Canvas(bar_frame, height=50, bg="#FFFFFF", highlightthickness=0)
        canvas.pack(fill="x", padx=20, pady=(15, 5))
        canvas.update_idletasks()
        w = canvas.winfo_width() or 500

        # Dessin des 4 segments colorés : Maigreur | Normal | Surpoids | Obésité
        segments = [
            (0, 0.25, "#3B82F6"),      # Bleu — Maigreur
            (0.25, 0.50, "#22C55E"),    # Vert — Normal
            (0.50, 0.75, "#F59E0B"),    # Jaune — Surpoids
            (0.75, 1.0, "#EF4444"),     # Rouge — Obésité
        ]
        for x0, x1, color in segments:
            canvas.create_rectangle(x0 * w, 5, x1 * w, 30, fill=color, outline="")

        # Curseur triangulaire indiquant la position de l'IMC sur la barre
        imc_clamped = max(10, min(40, imc))     # Borné entre 10 et 40 pour l'affichage
        mx = ((imc_clamped - 10) / 30) * w      # Conversion IMC → position en pixels
        canvas.create_polygon(mx - 8, 38, mx + 8, 38, mx, 30, fill="#1A1A2E")

        # ── Légendes sous la barre ──
        labels_frame = ctk.CTkFrame(bar_frame, fg_color="transparent")
        labels_frame.pack(fill="x", padx=20, pady=(0, 15))
        for text in ["< 18.5\nMaigreur", "18.5 – 24.9\nNormal",
                     "25 – 29.9\nSurpoids", "≥ 30\nObésité"]:
            ctk.CTkLabel(
                labels_frame, text=text,
                font=ctk.CTkFont(family=FONT_FAMILY, size=10),
                text_color=TEXT_MUTED, justify="center",
            ).pack(side="left", expand=True)
