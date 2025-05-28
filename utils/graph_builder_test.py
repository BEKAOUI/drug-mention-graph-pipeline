import pandas as pd
from collections import defaultdict
from typing import List, Dict, Any
import logging
from datetime import datetime
from utils.exporter import _format_output, _build_mention


logger = logging.getLogger(__name__)

class GraphBuilder:
    def __init__(self, drugs_clean: pd.DataFrame, pubmed_merge_clean: pd.DataFrame, clinical_clean: pd.DataFrame):
        self.drugs = drugs_clean
        self.pubmed = pubmed_merge_clean
        self.clinical = clinical_clean
        self.graph = defaultdict(list)

    def build(self) -> List[Dict[str, Any]]:
        for _, drug_row in self.drugs.iterrows():
            self._match_pubmed(drug_row)
            self._match_clinical(drug_row)
        logger.info(f"Graphe construit avec {len(self.graph)} journaux.")
        return _format_output(self.graph)

    def _match_pubmed(self, drug_row: pd.Series) -> None:
        matches = self.pubmed[
            self.pubmed["title"].str.contains(drug_row["drug"], na=False)
        ]
        for _, row in matches.iterrows():
            self.graph[row["journal"]].append(
                _build_mention(row, drug_row, source_type="pubmed")
            )

    def _match_clinical(self, drug_row: pd.Series) -> None:
        matches = self.clinical[
            self.clinical["scientific_title"].str.contains(drug_row["drug"], na=False)
        ]
        for _, row in matches.iterrows():
            self.graph[row["journal"]].append(
                _build_mention(row, drug_row, source_type="clinical_trial")
            )
