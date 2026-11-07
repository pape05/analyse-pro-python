import os
import collections
import customtkinter as ctk
from tkinter import filedialog, ttk
from utils import (
    FONT_FAMILY, ACCENT, SIDEBAR_ACTIVE, SUCCESS, DANGER, TEXT_DARK, TEXT_MUTED,
    card, section_title, extract_words,
)

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None


class PagePDF(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.pdf_path = None
        self.top10 = []
        self._build()

    def _build(self):
        c = card(self)
        c.pack(fill="x", pady=(0, 15))

        section_title(c, "📄", "Analyse de PDF").pack(padx=25, pady=(20, 10), anchor="w")

        drop_zone = ctk.CTkFrame(
            c, fg_color="#F0F7FF", corner_radius=12,
            border_width=2, border_color="#B8D4F0", height=120,
        )
        drop_zone.pack(padx=25, pady=10, fill="x")
        drop_zone.pack_propagate(False)

        ctk.CTkLabel(
            drop_zone, text="📥  Cliquez pour choisir un fichier PDF",
            font=ctk.CTkFont(family=FONT_FAMILY, size=14, weight="bold"),
            text_color=ACCENT,
        ).pack(expand=True, pady=(15, 0))

        ctk.CTkButton(
            drop_zone, text="Choisir un fichier",
            font=ctk.CTkFont(family=FONT_FAMILY, size=12),
            fg_color=ACCENT, hover_color=SIDEBAR_ACTIVE,
            corner_radius=8, height=35, width=160,
            command=self._charger,
        ).pack(pady=(0, 15))

        self.file_label = ctk.CTkLabel(
            c, text="",
            font=ctk.CTkFont(family=FONT_FAMILY, size=12), text_color=SUCCESS,
        )
        self.file_label.pack(padx=25, anchor="w")

        ctk.CTkButton(
            c, text="▶  Analyser le PDF",
            font=ctk.CTkFont(family=FONT_FAMILY, size=14, weight="bold"),
            fg_color=ACCENT, hover_color=SIDEBAR_ACTIVE,
            corner_radius=10, height=45,
            command=self._analyser,
        ).pack(padx=25, pady=15, fill="x")

        result_card = card(self)
        result_card.pack(fill="x")

        section_title(result_card, "🏆", "Top 10 des mots les plus fréquents").pack(
            padx=25, pady=(20, 10), anchor="w",
        )

        table_frame = ctk.CTkFrame(result_card, fg_color="transparent")
        table_frame.pack(padx=25, pady=(0, 20), fill="both")

        style = ttk.Style()
        style.configure(
            "PDF.Treeview", background="#FFFFFF", foreground=TEXT_DARK,
            fieldbackground="#FFFFFF", rowheight=32,
            font=(FONT_FAMILY, 12),
        )
        style.configure(
            "PDF.Treeview.Heading", background=ACCENT, foreground="#FFFFFF",
            font=(FONT_FAMILY, 12, "bold"), relief="flat",
        )
        style.map("PDF.Treeview.Heading", background=[("active", SIDEBAR_ACTIVE)])

        self.tree = ttk.Treeview(
            table_frame, columns=("rang", "mot", "freq"), show="headings",
            height=10, style="PDF.Treeview",
        )
        self.tree.heading("rang", text="#")
        self.tree.heading("mot", text="Mot")
        self.tree.heading("freq", text="Fréquence")
        self.tree.column("rang", width=50, anchor="center")
        self.tree.column("mot", width=250, anchor="w")
        self.tree.column("freq", width=150, anchor="center")
        self.tree.pack(fill="both", expand=True)

    def _charger(self):
        path = filedialog.askopenfilename(
            title="Choisir un fichier PDF",
            filetypes=[("Fichiers PDF", "*.pdf")],
        )
        if path:
            self.pdf_path = path
            self.file_label.configure(
                text=f"✅  Fichier chargé : {os.path.basename(path)}",
                text_color=SUCCESS,
            )

    def _analyser(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not self.pdf_path:
            self.file_label.configure(
                text="❌  Veuillez d'abord choisir un fichier PDF.", text_color=DANGER,
            )
            return

        if PdfReader is None:
            self.file_label.configure(
                text="❌  PyPDF2 n'est pas installé (pip install PyPDF2).", text_color=DANGER,
            )
            return

        try:
            reader = PdfReader(self.pdf_path)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        except Exception as e:
            self.file_label.configure(text=f"❌  Erreur de lecture : {e}", text_color=DANGER)
            return

        words = extract_words(text)
        if not words:
            self.tree.insert("", "end", values=("—", "Aucun mot trouvé", "—"))
            return

        counter = collections.Counter(words)
        total = sum(counter.values())
        self.top10 = counter.most_common(10)

        for i, (mot, count) in enumerate(self.top10, 1):
            freq = (count / total) * 100
            self.tree.insert("", "end", values=(i, mot, f"{freq:.2f} %"))
