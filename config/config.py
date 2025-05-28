DATA_PATHS = {
    "drugs" : "Data\\drugs.csv",
    "pubmed_csv" : "Data\\pubmed.csv",
    "pubmed_json" : "Data\\pubmed.json",
    "clinical_trials" : "data\\clinical_trials.csv"
}

LOG_FILE_PATH = "logs/pipeline.log"

required_columns_clinical_trials={"id", "scientific_title", "date", "journal"}
required_columns_pubmed={"id", "title", "date", "journal"}
required_columns_pubmed_json = {"id", "title", "date", "journal"}