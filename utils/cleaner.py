import pandas as pd
from datetime import datetime
import re
import uuid
import os
from utils.cleaning_helpers import (
    _validate_required_columns,
    _normalize_id,
    _clean_text_fields,
    _parse_and_validate_dates,
)
from utils.logger_utils import get_logger
logger = get_logger()

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

    #Etape 1: Validation des colonnes requises
    required_columns = {"id", "title", "date", "journal"}
    _validate_required_columns(df, required_columns, source_name="pubmed.csv")

    # Etape 2: Générer des IDs pour les lignes sans ID
    df = _normalize_id(df,source_name=source)

    
    # Nettoyage des lignes invalides
    df = _clean_text_fields(df, title_col="title", journal_col="journal", source_name=source)

    # enlever les espaces inutiles
    df['title'] = df['title'].str.strip()
    df['journal'] = df['journal'].str.strip()


    df = _parse_and_validate_dates(df, col="date", source_name=source)

    return df

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
    
    #Etape 1: Vérifier l'existance des colonnes
    required_columns = {"id","scientific_title","date","journal"}
    _validate_required_columns(df, required_columns, source_name=source)

    # Etape 2: Générer des IDs pour les lignes sans ID
    df = _normalize_id(df, source_name=source)
    
    
    # Sauvegarde des lignes invalides avant nettoyage
    df = _clean_text_fields(df, title_col="scientific_title", journal_col="journal", source_name=source)
    
   
    # Nettoyage des dates
    df = _parse_and_validate_dates(df, col="date", source_name=source)

    return df


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
     #Etape 1: Validation des colonnes requises
    required_columns = {"id", "title", "date", "journal"}
    _validate_required_columns(df, required_columns, source_name=source)

    # Etape 2: Générer des IDs pour les lignes sans ID
    df = _normalize_id(df, source_name=source)


    # Sauvegarde des lignes invalides avant nettoyage
    df = _clean_text_fields(df, title_col="title", journal_col="journal", source_name=source)

    # Nettoyage des dates
    df = _parse_and_validate_dates(df, col="date", source_name=source)

    return df

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