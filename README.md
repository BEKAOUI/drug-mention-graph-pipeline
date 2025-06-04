# drug-mention-graph-pipeline
Ce dépôt contient le code nécessaire à la préparation des données en vue de générer un graphe des mentions de médicaments dans les publications scientifiques (PubMed) et les essais cliniques (Clinical Trials), en les liant aux journaux médicaux.

## Étapes de préparation des données:
1. Collecte des données
Chargement des données provenant de différentes sources : fichiers CSV et JSON.

2. Nettoyage des données
Traitement des champs incohérents, normalisation des identifiants, unification des formats de date, etc.

3. Construction du graphe
Création d'un graphe reliant les médicaments aux publications et aux journaux où ils sont mentionnés.

4. Export du graphe
Sauvegarde du graphe final au format JSON dans le dossier output.
Ce travail est conçu pour être intégré dans un orchestrateur de type DAG.

 ## Intégration
Ce pipeline a été conçu pour être intégré dans un orchestrateur de type DAG (Directed Acyclic Graph), tel qu’Apache Airflow ou Prefect, facilitant son automatisation et sa planification.

##  Structure du projet
drug-mention-graph-pipeline/  
├── data /                     #donnee source : Données sources (CSV, JSON)  
├── cofig /                    #Fichiers de configuration (chemins, constantes, etc.)    
├── data_collection /           # Scripts pour charger et parser les données  
├── data_preparation /          # Nettoyage, normalisation et traitement des données   
├── graph_builder /             # Construction du graphe de mentions  
├── logs /                      # Fichiers de logs générés lors de l’exécution  
├── output /                    # Graphes générés en sortie (fichiers JSON)  
├── test /                      # Tests unitaires et de validation  
├── utils /                     # Fonctions atomiques partagées  
├── main.py                    # Point d’entrée principal du pipeline  
└── requirements.txt           # Dépendances Python du projet  

## Source de données

| Fichier               | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| `drugs.csv`           | Liste des médicaments, avec leur nom et leur code ATC.            |
| `pubmed.csv`          | Publications scientifiques issues de PubMed (format CSV).         |
| `pubmed.json`         | Autres publications scientifiques issues de PubMed (format JSON). |
| `clinical_trials.csv` | Données issues d’essais cliniques.                                |

Chaque source contient des métadonnées clés comme :
- id : identifiant unique de la publication ou de l’essai,
- title ou scientific_title : titre de l’étude,
- date : date de publication d'un article dans un journal,
- journal : nom du journal de publication,
- drug / atccode : dans le fichier drugs.csv, nom du médicament et son code ATC.

# Exécution du pipeline:
## Prérequis
Avant d'exécuter le pipeline, assurez-vous d'avoir:
 - Python 3.8+ installé
 - Création de l’environnement virtuel:

 | Commande  Création de l'environnement virtuel|
| --------------------------------------- |
| `python -m venv .venv`                  |

 
 - Activation de l'environnement:
   
 | Commande pour l'activation de l'environnement |
| --------------------------------------- |
| `.venv\Scripts\activate`                |


## Lancer le pipeline

 | Commande pour exécuter le pipeline |
| ---------------------------------- |
| `python main.py`                   |

  
- Le pipeline suit les étapes suivantes:
1. Chargement des données (drugs, pubmed, clinical_trials)
2. Nettoyage et normalisation des colonnes
3. Fusion des sources PubMed
4. Construction du graphe drug-mention
5. Export au format JSON dans output/graph.json

## Évolution du pipeline pour traiter de grandes volumiétries
Ce projet a été conçu pour fonctionner efficacement sur des fichiers de de petite taille. Cependant, pour faire évoluer le code afin qu'il puisse traiter des données à grande échelle (plusieurs To ou millions de fichiers), plusieurs améliorations sont nécessaires.
 
### Format de données adapté
- Limite actuelle : Les formats CSV / JSON ne sont pas optimisés pour la scalabilité (taille, compression, accès aléatoire inefficace).
- Recommandation :
 Remplacer ces formats par des alternatives plus performantes comme Parquet, Avro ou des bases NoSQL (type Bigtable, MongoDB).
 Ces formats sont mieux compressés, plus rapides à lire et à écrire, et adaptés aux traitements parallèles.

### Chargement mémoire
- Limite actuelle : pandas.read_csv() ou json.load() charge l'intégralité du fichier en mémoire, ce qui devient impossible pour des fichiers de plusieurs Go/To.
Recommandation : On peut Utiliser une lecture en streaming ou par morceaux (chunks) via pandas.read_csv(chunksize=...).

### Traitements parallèles ou distribués
- Limite actuelle : Traitement séquentiel sur une seule machine.
- Recommandation : On met en place du traitement parallèle local (via multiprocessing etc.).
  Passer à des frameworks distribués comme Apache Spark (via PySpark, Dataproc, etc.) pour exécuter les étapes sur un cluster de machines.

### Passage au Cloud et Big Data
- Recommandation : Utiliser un data lake (comme Google Cloud Storage, Azure Blob) pour le stockage distribué de fichiers.
  Déployer les traitements sur des services Big Data comme :
  Google Cloud Dataproc (Spark) ou Dataflow, Azure Synapse. Cela permet de profiter d’une scalabilité automatique, du calcul distribué, et de réduire les coûts sur les très gros volumes.

