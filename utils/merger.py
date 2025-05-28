# merger.py
import pandas as pd

def merge_pubmed_sources(pubmed_csv: pd.DataFrame, pubmed_json: pd.DataFrame) -> pd.DataFrame:
    """
    Fusionne les deux sources de publications scientifiques :
    - pubmed_csv : DataFrame issu du fichier CSV (pubmed.csv)
    - pubmed_json : DataFrame issu du fichier JSON (pubmed.json)
    """
    combined_df = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)
    return combined_df