import os
import json
import boto3
import pprint
import urllib.parse

if os.getenv("AWS_SAM_LOCAL"):
    dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url='http://host.docker.internal:4569/'
    )
    s3 = boto3.client(
        's3',
        endpoint_url='http://host.docker.internal:4572/'
    )
else:
    dynamodb = boto3.resource('dynamodb')
    s3 = boto3.client('s3')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("[bucket]: " + bucket + " [key]: " + key)

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        d = json.loads(response['Body'].read())
        pprint.pprint(d)
    except Exception as e:
        print(e)
        raise e