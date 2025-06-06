import json
import os
from typing import List, Dict, Any
import logging
from collections import defaultdict
import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)

def export_graph(graph_data: List[Dict[str, Any]], output_path: str = "output/graph.json") -> None:
    """
    Exports the graph data to a JSON file.
    
    Args:
        graph_data: Data to export (JSON-serializable list or dict)
        output_path: Path to the output file
    
    Raises:
        IOError: If writing to the file fails
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(graph_data, f, indent=2, ensure_ascii=False)
        logger.info(f"Graph exporté avec succès dans {output_path}")
    except Exception as e:
        logger.error(f"Erreur lors de l'export du graph : {str(e)}", exc_info=True)
        raise

def _format_output(journal_graph: defaultdict) -> List[Dict]:
    """Formats and sorts by date the final output """
    return sorted(
        [
            {
                "journal": journal,
                "mentions": sorted(mentions, key=lambda x: x["date"])
            }
            for journal, mentions in journal_graph.items()
        ],
        key=lambda x: x["journal"].lower()
    )

def _build_mention(row: pd.Series, drug_row: pd.Series, source_type: str) -> Dict[str, Any]:
    """Builds a standardized mention entry"""
    date_obj = row["date"] if isinstance(row["date"], datetime) else pd.to_datetime(row["date"])
    formatted_date = date_obj.strftime("%Y-%m-%d") if pd.notnull(date_obj) else "0000-00-00"
    return {
        "source": source_type,
        "date": formatted_date,
        "reference": str(row["id"]) if source_type == "pubmed" else row["id"],
        "drug": drug_row["drug"].upper(),
        "atccode": drug_row["atccode"],
        "title": row.get("title") or row.get("scientific_title")
    }
