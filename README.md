# Détection de faux profils sur les réseaux sociaux

## Objectif

Construire un modèle de Machine Learning capable de détecter automatiquement les faux profils sur les réseaux sociaux, à partir de caractéristiques extraites des comptes utilisateurs.

## Structure du projet

```
ML-faux-profils/
├── data/
│   ├── raw/          # Données brutes originales (non versionnées)
│   └── processed/    # Données nettoyées et transformées (non versionnées)
├── notebooks/        # Notebooks Jupyter d'exploration et d'analyse
├── src/              # Scripts Python (preprocessing, features, modèles)
├── models/           # Modèles entraînés (non versionnés)
├── webapp/
│   ├── templates/    # Templates HTML Flask
│   └── static/       # Fichiers CSS, JS, images
├── requirements.txt
└── README.md
```

## Installation

```bash
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
pip install -r requirements.txt
```
