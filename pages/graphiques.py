# ============================================================================
# graphiques.py — Page de visualisation graphique (Tâche 4)
# Affiche les résultats de l'analyse PDF sous forme de :
# - Diagramme circulaire (camembert) montrant la répartition des mots
# - Diagramme en barres montrant les fréquences comparées
# Utilise matplotlib intégré dans l'interface CustomTkinter.
# ============================================================================

import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils import (
    FONT_FAMILY, ACCENT, SIDEBAR_ACTIVE, DANGER, TEXT_MUTED,
    CHART_COLORS, card, section_title,
)


class PageGraphiques(ctk.CTkScrollableFrame):
    """
    Page de visualisation des résultats de l'analyse PDF.
    Récupère les données du top 10 via un callback vers la page PDF,
    puis génère deux graphiques matplotlib côte à côte.
    """

    def __init__(self, parent, get_pdf_top10):
        """
        Paramètres :
            parent : Widget parent (zone de contenu)
            get_pdf_top10 : Fonction callback qui retourne la liste
                            [(mot, count), ...] du top 10 de l'analyse PDF
        """
        super().__init__(parent, fg_color="transparent")
        self.get_pdf_top10 = get_pdf_top10
        self._build()

    def _build(self):
        """Construit le bouton d'actualisation et la zone d'affichage des graphiques."""
        self.graph_card = card(self)
        self.graph_card.pack(fill="x", pady=(0, 15))

        section_title(self.graph_card, "📊", "Visualisation des Résultats").pack(
            padx=25, pady=(20, 10), anchor="w",
        )

        # Bouton pour générer/actualiser les graphiques
        ctk.CTkButton(
            self.graph_card, text="🔄  Actualiser les graphiques",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13, weight="bold"),
            fg_color=ACCENT, hover_color=SIDEBAR_ACTIVE,
            corner_radius=10, height=40, width=250,
            command=self._draw,
        ).pack(padx=25, pady=(0, 15))

        # Conteneur pour les graphiques matplotlib
        self.container = ctk.CTkFrame(self.graph_card, fg_color="transparent")
        self.container.pack(padx=15, pady=(0, 20), fill="both")

        # Message d'information initial
        ctk.CTkLabel(
            self.container,
            text="ℹ️  Analysez d'abord un fichier PDF, puis cliquez sur « Actualiser les graphiques ».",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13), text_color=TEXT_MUTED,
        ).pack(pady=40)

    def _draw(self):
        """
        Génère les deux graphiques à partir des données du top 10 :
        - À gauche : diagramme circulaire avec légende
        - À droite : diagramme en barres avec étiquettes de fréquence
        """
        # Nettoyage des graphiques précédents
        for w in self.container.winfo_children():
            w.destroy()

        # Récupération des données depuis la page PDF
        top10 = self.get_pdf_top10()
        if not top10:
            ctk.CTkLabel(
                self.container,
                text="❌  Aucune donnée disponible. Analysez d'abord un fichier PDF (onglet Analyse PDF).",
                font=ctk.CTkFont(family=FONT_FAMILY, size=13), text_color=DANGER,
            ).pack(pady=40)
            return

        # Préparation des données pour les graphiques
        mots = [m for m, _ in top10]
        counts = [c for _, c in top10]
        total = sum(counts)
        freqs = [(c / total) * 100 for c in counts]    # Fréquences en pourcentage
        colors = CHART_COLORS[:len(mots)]               # Couleurs attribuées à chaque mot

        # Création de la figure matplotlib avec 2 sous-graphiques
        fig = Figure(figsize=(11, 4.5), dpi=100, facecolor="#FFFFFF")

        # ── Diagramme circulaire (à gauche) ──
        ax1 = fig.add_subplot(121)
        ax1.pie(
            freqs, labels=None, autopct="%1.1f%%", startangle=90,
            colors=colors, pctdistance=0.78,
            textprops={"fontsize": 8, "fontfamily": FONT_FAMILY},
        )
        # Légende positionnée à gauche du graphique
        ax1.legend(
            mots, loc="center left", bbox_to_anchor=(-0.35, 0.5),
            fontsize=8, frameon=False,
        )
        ax1.set_title(
            "Top 10 des mots (Diagramme circulaire)",
            fontsize=11, fontweight="bold", fontfamily=FONT_FAMILY, pad=15,
        )

        # ── Diagramme en barres (à droite) ──
        ax2 = fig.add_subplot(122)
        bars = ax2.bar(range(len(mots)), freqs, color=colors, width=0.65, edgecolor="none")
        ax2.set_xticks(range(len(mots)))
        ax2.set_xticklabels(mots, rotation=35, ha="right", fontsize=8, fontfamily=FONT_FAMILY)
        ax2.set_ylabel("Fréquence (%)", fontsize=9, fontfamily=FONT_FAMILY)
        ax2.set_title(
            "Top 10 des mots (Diagramme en barres)",
            fontsize=11, fontweight="bold", fontfamily=FONT_FAMILY, pad=15,
        )
        # Suppression des bordures supérieure et droite pour un style épuré
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_visible(False)

        # Étiquettes de fréquence au-dessus de chaque barre
        for bar, f in zip(bars, freqs):
            ax2.text(
                bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                f"{f:.1f}%", ha="center", fontsize=7,
                fontfamily=FONT_FAMILY, color=TEXT_MUTED,
            )

        fig.tight_layout(pad=2.5)

        # Intégration du graphique matplotlib dans l'interface Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
