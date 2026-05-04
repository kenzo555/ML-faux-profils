# Projet de Machine Learning — Détection de faux profils sur les réseaux sociaux

**Cadre** : Ingé2 — Majeure 2 D/DG — Année 2025-2026
**Domaine** : Big Data / Machine Learning supervisé (classification binaire)

---

## Descriptif

Les faux comptes sur les réseaux sociaux constituent un défi majeur pour toutes les plateformes (Instagram, Facebook, Twitter). Ils peuvent être à l'origine de désinformation, d'escroqueries ou encore d'automatisation de spam.

Certains comportements des utilisateurs tels que :
- le nombre de followers,
- le nombre de comptes suivis,
- le nombre de posts publiés par jour,
- le taux d'activité de spam,

peuvent être des indicateurs d'identification des faux profils.

---

## Objectif

Mettre en place une **application** permettant de détecter les faux profils sur les réseaux sociaux. Cette détection est basée sur :

1. L'exploration, l'analyse, la modélisation et le nettoyage d'un gros volume de données open data
2. L'entraînement et l'évaluation de différents modèles de Machine Learning
3. La sélection du modèle le plus performant
4. Le déploiement de ce modèle dans une application web

---

## Travail demandé

1. **Collecte des données** (base de données, scrapping, etc.)
2. **Exploration et analyse** des données pour mieux comprendre l'utilité de chaque attribut, puis sélection des features
3. **Implémentation** d'algorithmes pour la détection des faux profils
4. **Évaluation** des résultats de chaque algorithme pour choisir le meilleur modèle
5. **Implémentation d'une application web** qui utilise le modèle sélectionné pour détecter un faux profil

---

## Livrables

- Code source
- Démonstration

---

## Consignes spécifiques de l'enseignante

> ⚠️ **Important** — à respecter scrupuleusement :

- La base de données choisie au départ **ne doit pas être propre / déjà traitée**. Il faut un fichier CSV d'origine qui sera **traité par nous-mêmes** avant utilisation (preprocessing visible et justifié dans le rapport).
- Il faut **essayer plusieurs algorithmes du cours** avec **différents hyperparamètres** (utiliser GridSearchCV).
- Il faut **analyser les graphiques et les interpréter** (pas juste les afficher).
- Le site web doit fonctionner en **localhost**.
