from utils.loader import load_csv, load_json_as_dataframe
from utils.cleaner import clean_pubmed_csv, clean_clinical, clean_pubmed_json, clean_drugs_csv
from utils.merger import merge_pubmed_sources
from utils.graph_builder import build_graph
from utils.exporter import export_graph
from config.config import DATA_PATHS
from utils.logger_utils import get_logger

logger = get_logger()

def run_pipeline():
    logger.info("Début du pipeline de traitement des données")

    # Chargement des données
    logger.info("Chargement des données : drugs")

    drugs = load_csv(DATA_PATHS["drugs"])
    pubmed_csv = load_csv(DATA_PATHS["pubmed_csv"])
    pubmed_json = load_json_as_dataframe(DATA_PATHS["pubmed_json"])
    clinical = load_csv(DATA_PATHS["clinical_trials"])
    
    # Nettoyage
    logger.info("Nettoyage des données")

    pubmed_clean = clean_pubmed_csv(pubmed_csv)
    pubmed_json_clean = clean_pubmed_json(pubmed_json)
    clinical_clean = clean_clinical(clinical)
    drugs_clean = clean_drugs_csv(drugs)

    # Fusion PubMed
    pubmed_merged = merge_pubmed_sources(pubmed_clean, pubmed_json_clean)

    # Construction du graphe
    logger.info("Construction du graphe de données")
    graph_data = build_graph(drugs_clean, pubmed_merged, clinical_clean)

    # Export
    export_graph(graph_data, output_path="output/graph.json")

    # Methode 2
    #builder = GraphBuilder(drugs_clean, pubmed_merge, clinical_clean)
    #graph_data = builder.build()


if __name__ == "__main__":
    run_pipeline()