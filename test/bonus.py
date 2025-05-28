import json

def journal_avec_plus_unique_drug(json_path: str = "output/graph.json"):

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    max_journal = ""
    max_count = 0

    for entry in data:
        journal = entry["journal"]
        unique_drugs = {m["drug"] for m in entry["mentions"]}
        if len(unique_drugs) > max_count:
            max_count = len(unique_drugs)
            max_journal = journal

    return max_journal
