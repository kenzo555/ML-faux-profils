import pandas as pd
import numpy as np

SEED = 42
rng = np.random.default_rng(SEED)

df_original = pd.read_csv("data/raw/final-v1.csv")
df = df_original.copy()

n = len(df)

nan_username = rng.choice(df.index, size=int(n * 0.05), replace=False)
nan_fullname = rng.choice(df.index, size=int(n * 0.05), replace=False)
nan_follow = rng.choice(df.index, size=int(n * 0.03), replace=False)

df.loc[nan_username, "username_length"] = np.nan
df.loc[nan_fullname, "full_name_length"] = np.nan
df.loc[nan_follow, "edge_follow"] = np.nan

duplicates = df.sample(n=12, random_state=SEED)
df = pd.concat([df, duplicates], ignore_index=True)

outliers_username = rng.choice(df.index, size=5, replace=False)
outliers_fullname = rng.choice(df.index, size=3, replace=False)

df.loc[outliers_username, "username_length"] = [999, 888, 777, 666, 555]
df.loc[outliers_fullname, "full_name_length"] = [500, 600, 700]

na_string_idx = rng.choice(df.index, size=int(len(df) * 0.02), replace=False)
df["edge_followed_by"] = df["edge_followed_by"].astype(object)
df.loc[na_string_idx, "edge_followed_by"] = "N/A"

df.to_csv("data/raw/instagram_brut.csv", index=False)

print("=" * 55)
print("RÉCAPITULATIF DE DÉGRADATION")
print("=" * 55)
print(f"Lignes avant : {n}")
print(f"Lignes après  : {len(df)}")
print()
print("NaN introduits par colonne :")
print(f"  username_length  : {df['username_length'].isnull().sum()}")
print(f"  full_name_length : {df['full_name_length'].isnull().sum()}")
print(f"  edge_follow      : {df['edge_follow'].isnull().sum()}")
print()
print(f"Doublons avant : {df_original.duplicated().sum()}")
print(f"Doublons après : {df.duplicated().sum()}")
print()
print("Types après dégradation :")
print(df.dtypes)
