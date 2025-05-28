import pandas as pd
from config.config import required_columns_clinical_trials, required_columns_pubmed,required_columns_pubmed_json 
import re
import os
from utils.cleaning_helpers import (
    _validate_required_columns,
    _normalize_id,
    _clean_text_fields,
    _parse_and_validate_dates,
)
from utils.logger_utils import get_logger
logger = get_logger()

def _clean_generic(
    df: pd.DataFrame,
    required_columns: set,
    title_col: str,
    journal_col: str,
    date_col: str,
    source: str
) -> pd.DataFrame:
    """
    Fonction générique de nettoyage de DataFrame :
    - validation des colonnes
    - normalisation des IDs
    - nettoyage des champs texte
    - validation des dates
    """
    _validate_required_columns(df, required_columns, source_name=source)
    df = _normalize_id(df, source_name=source)
    df = _clean_text_fields(df, title_col=title_col, journal_col=journal_col, source_name=source)

    df[title_col] = df[title_col].str.strip()
    df[journal_col] = df[journal_col].str.strip()

    df = _parse_and_validate_dates(df, col=date_col, source_name=source)
    return df


def clean_pubmed_csv(df: pd.DataFrame, source: str = "pubmed_csv") -> pd.DataFrame:

    '''
    Nettoie le DataFrame PubMed issu d'un CSV avec gestion des erreurs.
    
    Args:
        df: DataFrame brut chargé depuis pubmed.csv
        log_path: Chemin pour enregistrer les lignes invalides
        
    Returns:
        DataFrame nettoyé
        
    Raises:
        ValueError: Si colonnes requises manquantes
    '''

    return _clean_generic(df, required_columns=required_columns_pubmed, title_col="title", journal_col="journal",date_col="date", source=source)

def clean_clinical(df: pd.DataFrame, source: str = "clinical_tials.csv") -> pd.DataFrame:
    '''
    Nettoie le DataFrame clinical_trials.csv issu d'un CSV avec gestion robuste des erreurs.
    
    Args:
        df: DataFrame brut chargé depuis clinical_tials.csv
        log_path: Chemin pour enregistrer les lignes invalides
        
    Returns:
        DataFrame nettoyé
        
    Raises:
        ValueError: Si colonnes requises manquantes
    '''

    return _clean_generic(df, required_columns=required_columns_clinical_trials, title_col="scientific_title", journal_col="journal",date_col="date", source=source)


def clean_pubmed_json(df: pd.DataFrame, source: str = "pubmed.json") -> pd.DataFrame:
    """
    Nettoie le DataFrame PubMed issu d'un json avec gestion robuste des erreurs.
    
    Args:
        df: DataFrame brut chargé depuis pubmed.json
        log_path: Chemin pour enregistrer les lignes invalides
        
    Returns:
        DataFrame nettoyé
        
    Raises:
        ValueError: Si colonnes requises manquantes
    """
    return _clean_generic(df, required_columns=required_columns_pubmed_json , title_col="title", journal_col="journal",date_col="date", source=source)

def clean_drugs_csv(df: pd.DataFrame, source: str = "drugs.csv") -> pd.DataFrame:
    """
        Nettoie le DataFrame drugs.csv issu d'un CSV avec gestion robuste des erreurs.
    
    Args:
        df: DataFrame brut chargé depuis drugs.csv
        log_path: Chemin pour enregistrer les lignes invalides
        
    Returns:
        DataFrame nettoyé
        
    Raises:
        ValueError: Si colonnes requises manquantes
    
    """

    #Etape 1: Validation des colonnes requises
    required_columns = {"atccode","drug"}
    _validate_required_columns(df, required_columns, source_name=source)
    # Création du répertoire de logs si inexistant
    df = _clean_text_fields(df, title_col="atccode", journal_col="drug", source_name=source)
    df = df.assign(drug_lower=df["drug"].str.lower())
    return df