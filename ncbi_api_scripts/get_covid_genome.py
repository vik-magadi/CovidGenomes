import requests
import zipfile
import io
import os
import json
from dotenv import load_dotenv
import boto3
import shutil

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

    # extract zip file and store it locally
    z = zipfile.ZipFile(io.BytesIO(genomeZip.content))
    z.extract("ncbi_dataset/data/genomic.fna", path="./genome_data/" + accession)
    
    upload_file_to_s3(accession)

    # delete file from local
    shutil.rmtree("./genome_data")

def upload_file_to_s3(accession):
    file_path = "./genome_data/" + accession + "/ncbi_dataset/data/genomic.fna"

    session = boto3.Session(
        aws_access_key_id=os.getenv("S3_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("S3_ACCESS_KEY_SECRET")
    )

    #Creating S3 Resource From the Session. 
    s3 = session.resource('s3')


    s3.Bucket(os.getenv("S3_BUCKET_NAME")).upload_file(file_path, accession + "_sequence.fna")
    
get_genome_data(wuhan_accession)



