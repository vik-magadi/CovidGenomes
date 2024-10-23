import requests

taxon = "2697049"

def get_genome_data(accession):
    payload = {
        "accessions":[accession],
        "taxon":"2697049",
        "include_sequence":["GENOME"],
        "aux_report":["DATASET_REPORT"],
        "format":"csv",
        "use_psg":False
    }
    headers= {
        "accept": "application/zip",
        "api-key": "6c1c34d9083e10e74a368375c29d9cdb5908",
        "content-type": "application/json",
    }
    return requests.post("https://api.ncbi.nlm.nih.gov/datasets/v2/virus/genome/download", data=payload, headers=headers)
