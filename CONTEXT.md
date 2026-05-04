# Contexte du projet — À lire AVANT toute action

> Ce fichier doit être lu par Claude Code au démarrage de chaque session pour cadrer ses suggestions et son code.

---

## 1. Profil de l'utilisatrice

- **Étudiante** : Kenza, 4e année d'école d'ingénieur, spécialisation Big Data
- **Niveau Python / ML** : intermédiaire, à l'aise avec pandas, scikit-learn, matplotlib, seaborn
- **Niveau Claude Code** : débutante — chaque commande doit être expliquée avant exécution
- **Travaille seule** sur ce projet

---

## 2. Préférences de travail

### Avant d'exécuter quoi que ce soit
- **Toujours expliquer en français** (2-3 phrases) ce que tu vas faire et pourquoi
- **Attendre confirmation explicite** avant d'exécuter une commande, créer/modifier un fichier
- **Procéder étape par étape**, jamais plusieurs actions enchaînées sans validation

### Style de code
- **Pas de commentaires inline** dans le code (Kenza préfère du code épuré)
- **Code lisible** plutôt que sur-optimisé
- **Variables et fonctions en français** ou anglais selon le contexte (rester cohérent)
- **Suivre les patterns vus en TP** (voir section 4 ci-dessous)

### Communication
- **Toujours en français**
- **Concision** : pas de longues digressions
- Si une erreur survient, **expliquer la cause avant de proposer le fix**

---

## 3. Cadre du projet

Lire `SUJET.md` à la racine pour le détail. En résumé :

- **Tâche** : classification binaire (vrai profil vs faux profil sur réseaux sociaux)
- **Dataset** : CSV brut Kaggle, à dégrader artificiellement si nécessaire pour respecter la consigne "données non traitées"
- **Plusieurs algorithmes** à comparer avec GridSearchCV
- **Web app Flask en localhost** pour la démo finale
- **Analyse et interprétation** des graphiques exigée

---

## 4. Algorithmes au programme du cours (À RESPECTER STRICTEMENT)

⚠️ **Ne JAMAIS proposer d'algorithmes hors programme** (l'enseignante note la cohérence avec le cours).

### ✅ Algorithmes autorisés

| Catégorie | Algorithmes |
|---|---|
| **Supervisé — classification** | LogisticRegression, KNeighborsClassifier, DecisionTreeClassifier |
| **Méthodes ensemblistes** | RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier |
| **Non supervisé (bonus)** | KMeans, MiniBatchKMeans |
| **Réduction de dimensions** | PCA |

### ❌ Algorithmes INTERDITS (hors programme)
- SVM (SVC, SVR)
- Naive Bayes
- XGBoost, LightGBM, CatBoost
- Réseaux de neurones (MLPClassifier, Keras, TensorFlow, PyTorch)
- Clustering hiérarchique, DBSCAN, etc.

---

## 5. Méthodologie attendue (basée sur les TP corrigés)

### Preprocessing
- Détection des valeurs manquantes : `df.isnull().sum()`
- Imputation : `SimpleImputer` (`strategy='mean'` pour numérique, `'most_frequent'` pour catégoriel)
- Encoding catégoriel : `LabelEncoder` ou `OneHotEncoder` selon le cas
- Normalisation : `StandardScaler` (par défaut), `MinMaxScaler` ou `RobustScaler` selon distribution

### Pipeline (pattern obligatoire)
Toujours utiliser `Pipeline` + `ColumnTransformer` quand il y a des features numériques ET catégorielles. Exemple type :

```python
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numerical_columns),
    ("cat", categorical_pipeline, categorical_columns)
])

model = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", LogisticRegression())
])
```

### Split train/test
- `train_test_split` avec `test_size=0.2` ou `0.25`, `random_state=42` (ou 123)

### Optimisation des hyperparamètres
- **Toujours** `GridSearchCV` avec `cv=5`
- Afficher `best_params_` et `best_score_`
- Récupérer le `best_estimator_` pour les prédictions finales

### Métriques (classification binaire)
**Toutes** ces métriques doivent être calculées et affichées :
- `accuracy_score`
- `precision_score`
- `recall_score`
- `f1_score`
- Matrice de confusion (`confusion_matrix`, à visualiser avec seaborn heatmap)
- Courbe ROC + AUC (`roc_curve`, `roc_auc_score`)
- `classification_report` (résumé global)

### Sélection de features
- Approche par `RandomForestClassifier().feature_importances_` (vue en TP)
- Visualisation via `plt.barh()`
- Optionnel : matrice de corrélation (`df.corr()` + heatmap)

### Réduction de dimensions (si pertinent)
- `PCA` avec choix du nombre de composantes via courbe cumulée de variance expliquée (méthode du coude)

---

## 6. Structure du projet

```
projet-faux-profils/
├── SUJET.md                    # Sujet officiel
├── CONTEXT.md                  # Ce fichier
├── README.md                   # Présentation du projet
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                    # CSV original (non modifié)
│   └── processed/              # CSV après nettoyage
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_comparison.ipynb
├── src/
│   ├── preprocessing.py
│   ├── models.py
│   └── utils.py
├── models/
│   └── best_model.pkl          # Modèle sérialisé (joblib)
└── webapp/
    ├── app.py                  # Flask
    ├── templates/
    │   └── index.html
    └── static/
```

---

## 7. Stack technique imposée

- **Python 3.10+**
- **scikit-learn** pour tous les algos ML
- **pandas** + **numpy** pour la manipulation
- **matplotlib** + **seaborn** pour la visualisation
- **Flask** pour la web app (localhost)
- **joblib** pour la sérialisation du modèle
- **jupyter** pour les notebooks d'exploration

---

## 8. Workflow de collaboration

1. Kenza discute la stratégie avec **Claude.ai** (autre fenêtre) avant chaque grosse étape
2. Elle copie-colle un **prompt précis** dans Claude Code
3. Claude Code **explique → demande validation → exécute**
4. En cas de problème, Kenza copie le retour vers Claude.ai pour ajustement

---

## 9. Rappels importants

- ⚠️ **Ne pas nettoyer le dataset trop vite** — le travail de preprocessing doit être visible et documenté
- ⚠️ **Ne pas utiliser un dataset déjà parfaitement propre** — c'est explicitement contre la consigne
- ⚠️ **Toujours interpréter les graphiques** — ne pas se contenter de les afficher
- ⚠️ **Tester plusieurs hyperparamètres** pour chaque algo via GridSearchCV
- ⚠️ **Comparer les modèles entre eux** dans une synthèse finale (tableau récapitulatif des métriques)
