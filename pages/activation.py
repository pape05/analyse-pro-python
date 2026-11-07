import customtkinter as ctk
from utils import (
    FONT_FAMILY, ACCENT, SUCCESS, DANGER, TEXT_DARK, TEXT_MUTED,
    PRODUCT_KEY, card,
)


class PageActivation(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self._build()

    def _build(self):
        c = card(self)
        c.pack(fill="x", pady=(0, 15), padx=50)

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

        self.key_entry = ctk.CTkEntry(
            c, width=400, height=45,
            font=ctk.CTkFont(family=FONT_FAMILY, size=14),
            placeholder_text="Votre clé de produit...", justify="center",
        )
        self.key_entry.pack(pady=(0, 15))

        ctk.CTkButton(
            c, text="✅  Activer",
            font=ctk.CTkFont(family=FONT_FAMILY, size=14, weight="bold"),
            fg_color=SUCCESS, hover_color="#218838",
            corner_radius=10, height=45, width=200,
            command=self._activer,
        ).pack(pady=(0, 10))

        self.label = ctk.CTkLabel(
            c, text="",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13),
        )
        self.label.pack(pady=(5, 25))

        ctk.CTkFrame(c, height=1, fg_color="#E2E8F0").pack(fill="x", padx=40, pady=5)

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
        key = self.key_entry.get().strip()
        if key == PRODUCT_KEY:
            self.label.configure(
                text="✅  Produit activé avec succès ! Merci.", text_color=SUCCESS,
            )
        else:
            self.label.configure(
                text="❌  Clé de produit invalide. Veuillez réessayer.", text_color=DANGER,
            )
