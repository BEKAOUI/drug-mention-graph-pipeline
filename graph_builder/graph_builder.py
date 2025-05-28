import pandas as pd
from collections import defaultdict
from typing import List, Dict, Any
import logging
from datetime import datetime
from utils.exporter import _format_output, _build_mention
logger = logging.getLogger(__name__)

def build_graph(drugs_clean: pd.DataFrame, pubmed_merge_clean: pd.DataFrame, clinical_clean: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    Construit le graphe de relations médicament-journaux avec mentions datées.
    
    Args:
        drugs: DataFrame des médicaments (atccode, drug)
        pubmed: DataFrame PubMed (id, title, date, journal)
        clinical: DataFrame Clinical Trials (id, scientific_title, date, journal)
    
    Returns:
        Liste de dictionnaires triés par journal et date
        
    Example de sortie:
        [{
            "journal": "Journal of...",
            "mentions": [
                {"source": "pubmed", "drug": "DIPHEN...", ...}
            ]
        }]
    """
    try:
        journal_graph = defaultdict(list)
        
        drugs_prep = drugs_clean.assign(drug_lower=drugs_clean["drug"].str.lower())

        for _, drug_row in drugs_prep.iterrows():
            # Recherche PubMed
            pubmed_matches = pubmed_merge_clean[
                pubmed_merge_clean["title"].str.lower().str.contains(drug_row["drug_lower"])
            ]
            for _, row in pubmed_matches.iterrows():
                journal_graph[row["journal"]].append(
                    _build_mention(row, drug_row, "pubmed")
                )
            
            # Recherche Clinical
            clinical_matches = clinical_clean[
                clinical_clean["scientific_title"].str.lower().str.contains(drug_row["drug_lower"])
            ]
            for _, row in clinical_matches.iterrows():
                journal_graph[row["journal"]].append(
                    _build_mention(row, drug_row, "clinical_trial")
                )

        return _format_output(journal_graph)

    except Exception as e:
        logger.error(f"Erreur dans build_graph: {str(e)}", exc_info=True)
        raise



