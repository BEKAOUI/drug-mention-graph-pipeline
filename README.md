# Drug Mention Graph Pipeline
This repository contains the code required to prepare the data for generating a graph of drug mentions in scientific publications (PubMed) and clinical trials, linking them to medical journals.

## Data Preparation Workflow:
1. Data Ingestion
Load raw data from multiple sources, including CSV and JSON files.

2. Data Cleaning
Perform field validation and correction, normalize identifiers, standardize date formats, and handle inconsistencies to ensure data quality.

3. Graph Construction
Build a directed graph that maps drugs to their mentions within scientific publications and associated journals.

4. Graph Export
Serialize and save the resulting graph structure in JSON format to the output folder for downstream processing.

 ## Integration
This pipeline is intended for integration within a DAG-based workflow orchestrator (e.g., Apache Airflow), allowing for automated, scheduled, and monitored data workflows.

##  Structure du projet
drug-mention-graph-pipeline/  
├── data /                     # Source data (CSV, JSON)  
├── config /                    # Configuration files (paths, constants, etc.)
├── data_collection /           # Scripts to load and parse data 
├── data_preparation /          # Data cleaning, normalization, and processing  
├── graph_builder /             # Construction of the drug-mention graph
├── logs /                      # Log files generated during execution  
├── output /                    # Generated graph outputs (JSON files) 
├── test /                      # Unit and validation tests  
├── utils /                     # Shared utility functions  
├── main.py                    # Main pipeline entry point 
└── requirements.txt           # Python dependencies for the project 

## Data Sources

| File                  | Description                                                   |
| --------------------- | ------------------------------------------------------------- |
| `drugs.csv`           | List of drugs with their names and ATC codes                  |
| `pubmed.csv`          | Scientific publications from PubMed (CSV format)              |
| `pubmed.json`         | Additional scientific publications from PubMed (JSON format)  |
| `clinical_trials.csv` | Data from clinical trials.                                    |


Each data source contains essential metadata including:

- id: a unique identifier for the publication or clinical trial,
- title or scientific_title: the study’s title,
- date: the date the article was published in the journal,
- journal: the name of the publishing journal,
- drug / atccode: in the drugs.csv file, the drug’s name and its ATC classification code.

# Pipeline Execution:
## Prerequisites
Before running the pipeline, please ensure you have:
- Python 3.8+ installed
- Created a virtual environment:

| Command to create the virtual environment |
| ----------------------------------------- |
| `python -m venv .venv`                    |


 
 - Activated the virtual environment:
   
| Command to activate the virtual environment |
| ------------------------------------------- |
| `.venv\Scripts\activate` (Windows)          |
| `source .venv/bin/activate` (Linux/macOS)   |


- Once activated, install the project dependencies:
  
| Command to install project dependencies |
| --------------------------------------- |
| `pip install -r requirements.txt`       |

## Run the pipeline

| Command to run the pipeline |
| --------------------------- |
| `python main.py`            |


  
- The pipeline follows these steps:
1. Data loading (drugs, pubmed, clinical_trials)
2. Cleaning and normalizing columns
3. Merging PubMed sources
4. Drug-mention graph construction
5. Exporting the graph as JSON to output/graph.json

## Pipeline Scalability for Large Volumes
This project was initially designed to efficiently process small-sized files. However, to scale it for large-scale data processing (several terabytes or millions of files), several improvements are necessary.
 
### Suitable Data Formats
- *Current limitation*: CSV and JSON formats are not optimized for scalability due to their size, compression inefficiency, and poor support for random access.
- *Recommendation*: 
 Replace these formats with more efficient alternatives such as Parquet, Avro, or NoSQL databases (e.g., Bigtable, MongoDB).
These formats offer better compression, faster read/write performance, and are well-suited for parallel processing.

### Memory-Efficient Loading
- *Current limitation*: pandas.read_csv() or json.load() loads the entire file into memory, which is not feasible for files of several gigabytes or terabytes.
- *Recommendation*:
  Use streaming or chunked loading with pandas.read_csv(chunksize=...) to process data in manageable portions.

### Parallel or Distributed Processing
- *Current limitation*: Sequential processing on a single machine.
- *Recommendation:*
Implement local parallelism (e.g., using Python’s multiprocessing module).
For larger scale, transition to distributed frameworks such as Apache Spark (via PySpark, Dataproc, etc.) to run processing steps on a cluster.

### Cloud and Big Data Adoption
- *Recommendation*:
Store data in a data lake such as Google Cloud Storage or Azure Blob Storage to enable distributed file storage.
Run processing jobs on Big Data services like Google Cloud Dataproc (Spark), Dataflow, or Azure Synapse Analytics.
These platforms provide automatic scalability, distributed computing, and cost efficiencies for very large volumes of data.

