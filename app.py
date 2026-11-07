import customtkinter as ctk

import matplotlib
matplotlib.use("TkAgg")

from utils import (
    SIDEBAR_BG, SIDEBAR_HOVER, SIDEBAR_ACTIVE, HEADER_BG,
    MAIN_BG, SUCCESS, TEXT_MUTED, FONT_FAMILY,
)
from pages import (
    PageAccueil, PageIMC, PageTexte, PagePDF, PageGraphiques, PageActivation,
)


class SidebarButton(ctk.CTkButton):
    def __init__(self, master, text, icon, command, **kwargs):
        super().__init__(
            master, text=f"  {icon}  {text}", command=command,
            font=ctk.CTkFont(family=FONT_FAMILY, size=14),
            fg_color="transparent", text_color="#B0C4DE",
            hover_color=SIDEBAR_HOVER, anchor="w",
            height=45, corner_radius=10, **kwargs,
        )

    def set_active(self, active):
        if active:
            self.configure(fg_color=SIDEBAR_ACTIVE, text_color="#FFFFFF")
        else:
            self.configure(fg_color="transparent", text_color="#B0C4DE")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Analyse Pro Python v1.0")
        self.geometry("1380x820")
        self.minsize(1200, 700)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_main_area()
        self._build_status_bar()
        self._create_pages()
        self.show_page("accueil")

    # ─── Sidebar ─────────────────────────────────────────────────
    def _build_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=180, fg_color=SIDEBAR_BG, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns", rowspan=2)
        self.sidebar.grid_propagate(False)

        logo_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo_frame.pack(pady=(25, 5), padx=10)
        ctk.CTkLabel(logo_frame, text="🐍", font=ctk.CTkFont(size=40), text_color="#FFFFFF").pack()
        ctk.CTkLabel(
            logo_frame, text="Analyse Pro\nPython",
            font=ctk.CTkFont(family=FONT_FAMILY, size=16, weight="bold"),
            text_color="#FFFFFF", justify="center",
        ).pack(pady=(5, 0))
        ctk.CTkLabel(
            logo_frame, text="Analyse • Calcule • Visualise",
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, slant="italic"),
            text_color="#7B9CC4",
        ).pack(pady=(2, 0))

        ctk.CTkFrame(self.sidebar, height=1, fg_color="#1E3F7A").pack(fill="x", padx=15, pady=15)

        self.sidebar_buttons = {}
        nav_items = [
            ("accueil", "Accueil", "🏠"),
            ("imc", "Calcul IMC", "⚖️"),
            ("texte", "Analyse Texte", "📝"),
            ("pdf", "Analyse PDF", "📄"),
            ("graphiques", "Graphiques", "📊"),
            ("activation", "Activation", "🔑"),
        ]
        for key, label, icon in nav_items:
            btn = SidebarButton(self.sidebar, label, icon, lambda k=key: self.show_page(k))
            btn.pack(fill="x", padx=10, pady=3)
            self.sidebar_buttons[key] = btn

        ctk.CTkFrame(self.sidebar, fg_color="transparent").pack(fill="both", expand=True)
        ctk.CTkLabel(
            self.sidebar, text="Un outil puissant\npour analyser vos données",
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, slant="italic"),
            text_color="#5A7BA6", justify="center",
        ).pack(pady=(0, 20))

    # ─── Zone principale ─────────────────────────────────────────
    def _build_main_area(self):
        self.main_container = ctk.CTkFrame(self, fg_color=MAIN_BG, corner_radius=0)
        self.main_container.grid(row=0, column=1, sticky="nsew")
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(1, weight=1)

        self.header = ctk.CTkFrame(self.main_container, height=80, fg_color=HEADER_BG, corner_radius=0)
        self.header.grid(row=0, column=0, sticky="ew")
        self.header.grid_propagate(False)

        self.header_title = ctk.CTkLabel(
            self.header, text="",
            font=ctk.CTkFont(family=FONT_FAMILY, size=22, weight="bold"),
            text_color="#FFFFFF",
        )
        self.header_title.pack(side="left", padx=25, pady=10)

        self.header_subtitle = ctk.CTkLabel(
            self.header, text="",
            font=ctk.CTkFont(family=FONT_FAMILY, size=12), text_color="#9BB5D6",
        )
        self.header_subtitle.place(x=25, y=48)

        self.content = ctk.CTkFrame(self.main_container, fg_color=MAIN_BG, corner_radius=0)
        self.content.grid(row=1, column=0, sticky="nsew", padx=20, pady=15)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

    # ─── Barre de statut ─────────────────────────────────────────
    def _build_status_bar(self):
        status = ctk.CTkFrame(self, height=30, fg_color="#E2E8F0", corner_radius=0)
        status.grid(row=1, column=0, columnspan=2, sticky="ew")
        status.grid_propagate(False)
        ctk.CTkLabel(
            status, text="●  Application prête à l'emploi",
            font=ctk.CTkFont(family=FONT_FAMILY, size=11), text_color=SUCCESS,
        ).pack(side="left", padx=15)
        ctk.CTkLabel(
            status, text="Analyse Pro Python v1.0  |  Développé en Python",
            font=ctk.CTkFont(family=FONT_FAMILY, size=11), text_color=TEXT_MUTED,
        ).pack(side="right", padx=15)

    # ─── Pages ───────────────────────────────────────────────────
    def _create_pages(self):
        self.page_pdf = PagePDF(self.content)
        self.pages = {
            "accueil": PageAccueil(self.content, self.show_page),
            "imc": PageIMC(self.content),
            "texte": PageTexte(self.content),
            "pdf": self.page_pdf,
            "graphiques": PageGraphiques(self.content, lambda: self.page_pdf.top10),
            "activation": PageActivation(self.content),
        }

    def show_page(self, name):
        for key, btn in self.sidebar_buttons.items():
            btn.set_active(key == name)

        for widget in self.content.winfo_children():
            widget.pack_forget()

        headers = {
            "accueil": ("Bienvenue sur Analyse Pro Python !",
                        "Une application complète pour calculer votre IMC, analyser vos textes et vos fichiers PDF."),
            "imc": ("Calcul de l'IMC", "Connaissez votre indice de masse corporelle"),
            "texte": ("Analyse de Texte", "Découvrez les mots de plus de 4 lettres"),
            "pdf": ("Analyse de PDF", "Trouvez les 10 mots les plus fréquents"),
            "graphiques": ("Visualisation des Résultats", "Diagrammes circulaire et en barres"),
            "activation": ("Activation du Produit", "Entrez votre clé de produit pour activer l'application"),
        }
        title, subtitle = headers.get(name, ("", ""))
        self.header_title.configure(text=title)
        self.header_subtitle.configure(text=subtitle)

        if name in self.pages:
            self.pages[name].pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
