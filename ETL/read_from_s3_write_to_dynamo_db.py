import os
import json
from dotenv import load_dotenv
import boto3

# read the file from s3 and create a dictionary with the mapping:
# {"accession": <accession> "sequence": "AGCTA"}

def read_from_s3(accession):
    session = boto3.Session(
        aws_access_key_id=os.getenv("S3_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("S3_ACCESS_KEY_SECRET")
    )

    s3 = session.resource('s3')

    s3.Bucket(os.getenv("S3_BUCKET_NAME"))

