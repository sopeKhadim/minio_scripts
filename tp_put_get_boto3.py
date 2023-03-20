#!/usr/bin/env/python
import os
import boto3
import configparser
from botocore.exceptions import ClientError

config = configparser.ConfigParser()
config.read('credentials.ini')

# Set the credentials with credentials.ini #
URL_API = config['minio']['url_api']
ACCES_KEY = config['minio']['acces_key']
SECRET_KEY = config['minio']['secret_key']
SECURE = config['minio']['secret']
TOKEN = config['minio']['token']

client = boto3.resource('s3',
                        endpoint_url=URL_API,
                        aws_access_key_id=ACCES_KEY,
                        aws_secret_access_key=SECRET_KEY,
                        aws_session_token=TOKEN,
                        config=boto3.session.Config(signature_version='s3v4'),
                        verify=SECURE
                        )

# Upload file into MinIO

try:
    client.upload_file('/path/from/source/filename',
                       'bucket_name',
                       'object_name')
except ClientError as e:
    print(e)

# Download the object from the bucket 'bucket_name' and
# save it to local FS  /path/to/target/filename
try:
    client.download_file('bucket_name',
                         'object_name',
                         '/path/to/source/filename')

except ClientError as e:
    print(e)
