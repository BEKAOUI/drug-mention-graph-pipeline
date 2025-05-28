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
├── data /    #donnee source : Données sources (CSV, JSON)  
├── cofig /   #Fichiers de configuration (chemins, constantes, etc.)  
          
