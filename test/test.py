from pathlib import Path
from loader import load_csv,load_json_as_dataframe
from cleaner import clean_pubmed, clean_clinical, clean_pubmed_json

pubmed_csv = Path("C:/Users\Bekao\OneDrive\Bureau\Python_test_DE v2.0\projet_SERVIER\Data_pipeline\data\pubmed.csv")

df = load_csv("C:/Users/Bekao/OneDrive/Bureau/Python_test_DE v2.0/projet_SERVIER/Data_pipeline/data/pubmed.csv")

df_clean = clean_pubmed(df)
print(df_clean)

df_t= load_csv("C:/Users/Bekao/OneDrive/Bureau/Python_test_DE v2.0/projet_SERVIER/Data_pipeline/data/clinical_trials.csv")

df_t_clean = clean_clinical(df_t)


df = load_json_as_dataframe("C:/Users/Bekao/OneDrive/Bureau/Python_test_DE v2.0/projet_SERVIER\/Data_pipeline/data/pubmed.json")
df_test= clean_pubmed_json(df)

print(df_test)

print("pubmed:", df.isnull().sum())