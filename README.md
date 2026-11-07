# Analyse Pro Python v1.0

Application desktop Python avec interface graphique permettant de calculer l'IMC, analyser des textes et extraire les mots les plus fréquents de fichiers PDF.

> Projet réalisé dans le cadre de la Licence 2 Génie Informatique — UNIPRO

## Fonctionnalités

| Tâche | Description |
|-------|-------------|
| **Calcul IMC** | Saisie du poids et de la taille, calcul de l'IMC avec interprétation (maigreur, normal, surpoids, obésité) et barre visuelle colorée |
| **Analyse de Texte** | Coller un texte pour extraire les mots de plus de 4 lettres avec leur fréquence en pourcentage dans un tableau structuré |
| **Analyse PDF** | Charger un fichier PDF et afficher les 10 mots les plus fréquents (> 4 lettres) par ordre décroissant |
| **Graphiques** | Visualisation des résultats PDF sous forme de diagramme circulaire et diagramme en barres |
| **Activation** | Système d'activation par clé de produit |

## Aperçu

L'application dispose d'une interface moderne avec :
- Une barre de navigation latérale (sidebar)
- Un système d'onglets pour naviguer entre les fonctionnalités
- Un dashboard d'accueil avec accès rapide à toutes les fonctionnalités
- Une barre de statut

## Technologies utilisées

- **Python 3** — Langage principal
- **CustomTkinter** — Interface graphique moderne
- **Matplotlib** — Génération des graphiques (diagramme circulaire et en barres)
- **PyPDF2** — Extraction du texte depuis les fichiers PDF

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/pape05/analyse-pro-python.git
cd analyse-pro-python
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l'application

```bash
python app.py
```

## Structure du projet

```
analyse-pro-python/
├── app.py              # Point d'entrée — fenêtre principale et navigation
├── utils.py            # Constantes (couleurs, police) et fonctions partagées
├── pages/
│   ├── __init__.py     # Exports des pages
│   ├── accueil.py      # Page d'accueil (dashboard)
│   ├── imc.py          # Calcul de l'IMC
│   ├── texte.py        # Analyse de texte collé
│   ├── pdf.py          # Analyse de fichier PDF
│   ├── graphiques.py   # Visualisation graphique
│   └── activation.py   # Activation par clé de produit
└── requirements.txt    # Dépendances Python
```

## Clé d'activation

```
ANALYSE-PRO-2024-PYTHON-LIC3
```
