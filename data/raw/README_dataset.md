# Documentation du dataset

## Source originale

- **Nom** : Instagram Fake and Real Accounts Dataset
- **URL** : https://www.kaggle.com/datasets/rezaunderfit/instagram-fake-and-real-accounts-dataset
- **Fichier original** : `final-v1.csv` (785 lignes, 13 colonnes)
- **Cible** : `is_fake` — 1 = faux profil, 0 = vrai profil

---

## Justification de la dégradation

Le dataset Kaggle original est trop propre (0 valeur manquante, types cohérents) pour satisfaire la consigne de l'enseignante qui exige un fichier CSV brut nécessitant un preprocessing visible et documenté.

Un script de dégradation volontaire (`src/degrade_dataset.py`) a été appliqué sur une copie du fichier original pour introduire des imperfections représentatives de problèmes réels. Cette démarche est transparente et documentée ici.

Le fichier original `final-v1.csv` n'est jamais modifié. Le script repart toujours de ce fichier source, garantissant la reproductibilité.

---

## Imperfections introduites

| Type | Colonne | Quantité |
|---|---|---|
| Valeurs manquantes (NaN) | `username_length` | ~5% des lignes (~39 NaN) |
| Valeurs manquantes (NaN) | `full_name_length` | ~5% des lignes (~39 NaN) |
| Valeurs manquantes (NaN) | `edge_follow` | ~3% des lignes (~24 NaN) |
| Doublons exacts | toutes colonnes | +12 lignes dupliquées |
| Outliers extrêmes | `username_length` | 5 valeurs (999, 888, 777, 666, 555) |
| Outliers extrêmes | `full_name_length` | 3 valeurs (500, 600, 700) |
| Type incohérent (object) | `edge_followed_by` | ~2% remplacés par la chaîne "N/A" |

---

## Reproductibilité

- **Random seed** : `42` (utilisé via `numpy.random.default_rng(42)` et `DataFrame.sample(random_state=42)`)
- Toute réexécution de `src/degrade_dataset.py` produit exactement le même fichier `instagram_brut.csv`

---

## Fichiers

| Fichier | Description |
|---|---|
| `final-v1.csv` | Dataset original Kaggle — ne pas modifier |
| `instagram_brut.csv` | Version dégradée — point de départ du projet |
