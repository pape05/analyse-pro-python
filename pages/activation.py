# ============================================================================
# activation.py — Page d'activation du produit (Tâche 5)
# Permet à l'utilisateur d'entrer une clé de produit pour activer
# l'application. Vérifie la clé saisie et affiche le résultat.
# ============================================================================

import customtkinter as ctk
from utils import (
    FONT_FAMILY, ACCENT, SUCCESS, DANGER, TEXT_DARK, TEXT_MUTED,
    PRODUCT_KEY, card,
)


class PageActivation(ctk.CTkFrame):
    """
    Page d'activation par clé de produit.
    L'utilisateur saisit une clé dans le champ de texte.
    Si la clé correspond à PRODUCT_KEY, l'activation est confirmée.
    Sinon, un message d'erreur est affiché.
    """

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self._build()

    def _build(self):
        """Construit le formulaire d'activation avec le champ de saisie et le bouton."""
        c = card(self)
        c.pack(fill="x", pady=(0, 15), padx=50)

        # ── Icône et titre ──
        ctk.CTkLabel(c, text="🔑", font=ctk.CTkFont(size=48)).pack(pady=(30, 10))
        ctk.CTkLabel(
            c, text="Activation du Produit",
            font=ctk.CTkFont(family=FONT_FAMILY, size=20, weight="bold"),
            text_color=TEXT_DARK,
        ).pack()
        ctk.CTkLabel(
            c, text="Entrez votre clé de produit pour activer l'application.",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13), text_color=TEXT_MUTED,
        ).pack(pady=(5, 20))

        # ── Champ de saisie de la clé ──
        self.key_entry = ctk.CTkEntry(
            c, width=400, height=45,
            font=ctk.CTkFont(family=FONT_FAMILY, size=14),
            placeholder_text="Votre clé de produit...", justify="center",
        )
        self.key_entry.pack(pady=(0, 15))

        # ── Bouton d'activation ──
        ctk.CTkButton(
            c, text="✅  Activer",
            font=ctk.CTkFont(family=FONT_FAMILY, size=14, weight="bold"),
            fg_color=SUCCESS, hover_color="#218838",
            corner_radius=10, height=45, width=200,
            command=self._activer,
        ).pack(pady=(0, 10))

        # Label pour afficher le résultat de l'activation
        self.label = ctk.CTkLabel(
            c, text="",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13),
        )
        self.label.pack(pady=(5, 25))

        # ── Séparateur ──
        ctk.CTkFrame(c, height=1, fg_color="#E2E8F0").pack(fill="x", padx=40, pady=5)

        # ── Affichage de la clé de produit (pour faciliter les tests) ──
        ctk.CTkLabel(
            c, text="Clé de produit :",
            font=ctk.CTkFont(family=FONT_FAMILY, size=12, weight="bold"),
            text_color=TEXT_DARK,
        ).pack(pady=(15, 5))
        ctk.CTkLabel(
            c, text=PRODUCT_KEY,
            font=ctk.CTkFont(family="Consolas", size=14), text_color=ACCENT,
        ).pack(pady=(0, 20))

    def _activer(self):
        """Vérifie la clé saisie et affiche le résultat (succès ou erreur)."""
        key = self.key_entry.get().strip()
        if key == PRODUCT_KEY:
            self.label.configure(
                text="✅  Produit activé avec succès ! Merci.", text_color=SUCCESS,
            )
        else:
            self.label.configure(
                text="❌  Clé de produit invalide. Veuillez réessayer.", text_color=DANGER,
            )
