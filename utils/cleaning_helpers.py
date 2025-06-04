import pandas as pd
from typing import List, Dict
from typing import List, Dict, Any
from datetime import datetime
from utils.logger_utils import get_logger

logger = get_logger()

def _validate_required_columns(df: pd.DataFrame, required_columns: set, source_name: str):
    """
    Checks whether the expected columns are present in the DataFrame.
    Raises an explicit error if any are missing.
    """
    missing = required_columns - set(df.columns)
    if missing:
        msg = f"[{source_name}] Vérification échouée : colonnes manquantes détectées → {missing}"

        logger.error(msg)
        raise ValueError(msg)

def _normalize_id(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """
     Normalizes IDs in the clinical_trials and PubMed files:
    - Strips whitespace
    """
    missing_mask = df["id"].astype(str).str.strip().isin(["", "nan", "None"])

    if missing_mask.any():
        logger.warning(
            f"[{source_name}] Champs 'id' vide ou null détecté (ligne = {df[missing_mask]})."
        )
        
    
    # Data entries without 'id' are intentionally processed to avoid data loss
    return df

def _clean_text_fields(df: pd.DataFrame, title_col: str, journal_col: str, source_name :str) -> pd.DataFrame:
    df[title_col] = df[title_col].str.strip().str.lower()
    df[journal_col] = df[journal_col].str.strip().str.title()
    
    invalid = df[df[title_col].isnull() | df[journal_col].isnull()]
    
    if not invalid.empty:
        logger.warning(
            f"[{source_name}] Les Champs {title_col} ou {journal_col} vide ou null détecté (ligne = {invalid})."
        )
    return df.dropna(subset=[title_col, journal_col])

def _parse_and_validate_dates(df: pd.DataFrame, col: str, source_name: str) -> pd.DataFrame:
    df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True)
    invalid = df[df[col].isnull()]
    
    if not invalid.empty:
        logger.warning(
            f"[{source_name}] Les Champs 'date' est invalide (ligne = {invalid})."
        )
    # Data entries without 'date' are intentionally processed to avoid data loss
    return df

