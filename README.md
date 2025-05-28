# drug-mention-graph-pipeline
Pipeline de données permettant de générer un graphe des mentions de médicaments dans les publications scientifiques (PubMed) et essais cliniques (Clinical Trials), lié aux journaux médicaux.

## Objectif
Ce projet extrait, nettoie, fusionne et structure les données de publications scientifiques et d’essais cliniques afin de produire un fichier JSON représentant les mentions de médicaments dans différents journaux. Il est conçu pour être intégré dans un orchestrateur de type DAG.

##  Structure du projet
drug-mention-graph-pipeline/

├── main.py                  # Exécution principale

├── config/                 # Configurations des variable globales

├── data/                   # Données d'entrée CSV/

├── logs/                   # Fichiers de logs générés
├── output/                 # Résultat final (graph.json)
├── tests/                  # Tests unitaires (pytest)
├── utils/                  # Modules métiers (loader, cleaner, atomques.)
├── requirements.txt        # Dépendances Python
└── README.md               
