import pandas as pd
import numpy as np
import json
import os
import re
from typing import Union
from utils.logger_utils import get_logger

logger = get_logger()

def load_csv(path: str, encoding: str = "utf-8") -> pd.DataFrame:
    """
    Charge un fichier CSV et retourne un DataFrame.
    Log une erreur claire si le fichier est manquant ou invalide.
    """
    if not os.path.exists(path):
        msg = f"[load_csv] Fichier introuvable : {path}"
        logger.error(msg)
        raise FileNotFoundError(msg)

    try:
        df = pd.read_csv(path, encoding=encoding)
    except Exception as e:
        msg = f"[load_csv] Erreur de lecture CSV ({path}) : {e}"
        logger.error(msg)
        raise ValueError(msg)

    return df

def load_json_as_dataframe(path: str) -> pd.DataFrame:
    """
    Charge un fichier JSON contenant une liste d'objets
    et retourne un DataFrame. Log les erreurs de parsing.
    """
    if not os.path.exists(path):
        msg = f"[load_json_as_dataframe] Fichier introuvable : {path}"
        logger.error(msg)
        raise FileNotFoundError(msg)

    try:
        with open(path, encoding="utf-8") as f:
            cleaned_json_str = remove_misplaced_commas(f.read())
            data = json.loads(cleaned_json_str)

            if not isinstance(data, list):
                msg = "[load_json_as_dataframe] Le format du fichier json est invaide!"
                logger.error(msg)
                raise ValueError(msg)
            return pd.DataFrame(data)
            
    except json.JSONDecodeError as e:
        msg = f"[load_json_as_dataframe] JSON invalide ({path}) : {e}"
        logger.error(msg)
        raise ValueError(msg)
    except Exception as e:
        msg = f"[load_json_as_dataframe] Erreur({path}) : {e}"
        logger.error(msg)
        raise ValueError(msg)

def remove_misplaced_commas(json_str):
   # enlever les virgules mal placées ( ',)' ou ',]' )
    cleaned_json = re.sub(r',\s*([}\]])', r'\1', json_str)
    return cleaned_json

