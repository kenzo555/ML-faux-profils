# Dataset — Détection de faux profils sur réseaux sociaux

## Fichier
- Nom : `fake_social_media_global_2_0_with_missing.xlsx`
- Format : Excel
- Lignes : 3000
- Colonnes : 24

## Source
Dataset partagé par mon camarade de promotion (sourcé sur Kaggle).

## Variable cible
`is_fake` : 0 = vrai profil (1941 cas, 64,7%), 1 = faux profil (1059 cas, 35,3%)

## Caractéristique notable
Le dataset est **déjà brut** d'origine (avec des valeurs manquantes injectées sur la plupart des colonnes), ce qui correspond exactement à la consigne de l'enseignante qui demandait un fichier non traité à nettoyer soi-même. Pas besoin de dégradation artificielle ici.

## Colonnes
**Caractéristiques du compte** : platform, has_profile_pic, bio_length, verified, account_age_days

**Activité** : followers, following, follower_following_ratio, posts, posts_per_day

**Comportements suspects** : caption_similarity_score, content_similarity_score, follow_unfollow_rate, spam_comments_rate, generic_comment_rate, suspicious_links_in_bio

**Caractéristiques username** : username_randomness, username_length, digits_count, digit_ratio, special_char_count, repeat_char_count

**Variable cible** : is_fake

**Variable à exclure de la modélisation** : username (identifiant non prédictif)
