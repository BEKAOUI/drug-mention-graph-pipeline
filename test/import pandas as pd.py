import pandas as pd
# Lecture des fichiers
df_drugs = pd.read_csv("C:/Users/Bekao/OneDrive/Bureau/Python_test_DE v2.0/projet_SERVIER/Data/drugs.csv")
df_pubmed = pd.read_csv("C:/Users/Bekao/OneDrive/Bureau/Python_test_DE v2.0/projet_SERVIER/Data/pubmed.csv")
df_clinical = pd.read_csv("C:/Users/Bekao/OneDrive/Bureau/Python_test_DE v2.0/projet_SERVIER/Data/clinical_trials.csv")

# Aperçu rapide
print("=== drugs.csv ===")
print(df_drugs.head(), end="\n\n")

print("=== pubmed.csv ===")
print(df_pubmed.head(), end="\n\n")

print("=== clinical_trials.csv ===")
print(df_clinical.head(), end="\n\n")

# Vérification des nulls
print("=== Nulls ===")
print("drugs:", df_drugs.isnull().sum())
print("pubmed:", df_pubmed.isnull().sum())
print("clinical:", df_clinical.isnull().sum())