import pandas as pd

def merge_pubmed_sources(pubmed_csv: pd.DataFrame, pubmed_json: pd.DataFrame) -> pd.DataFrame:
    """
    Merges the two sources of scientific publications:
    - pubmed_csv: DataFrame from the CSV file (pubmed.csv)
    - pubmed_json: DataFrame from the JSON file (pubmed.json)
    """
    combined_df = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)
    return combined_df
