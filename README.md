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
