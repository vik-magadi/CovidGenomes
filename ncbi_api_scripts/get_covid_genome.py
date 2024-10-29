import requests
import zipfile
import io
import os
import json
from dotenv import load_dotenv

load_dotenv()

taxon = "2697049"
wuhan_accession = "NC_045512.2"

def get_genome_data(accession):
    data = {
        "accessions":[accession],
        "taxon": taxon,
        "include_sequence":["GENOME"],
        "aux_report":["DATASET_REPORT"],
        "format":"csv",
    }

    headers= {
        "accept": "application/zip",
        "api-key": "6c1c34d9083e10e74a368375c29d9cdb5908",
        "content-type": "application/json",
    }

    genomeZip = requests.post("https://api.ncbi.nlm.nih.gov/datasets/v2/virus/genome/download", data=json.dumps(data), headers=headers)
    z = zipfile.ZipFile(io.BytesIO(genomeZip.content))
    z.extract("ncbi_dataset/data/genomic.fna", path="./genome_data/" + accession)
    
get_genome_data(wuhan_accession)



