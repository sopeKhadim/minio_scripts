import configparser
from minio import Minio
from minio.select import (CSVInputSerialization,
                          CSVOutputSerialization,
                          SelectRequest)


config = configparser.ConfigParser()
config.read('credentials.ini')

# Set the credentials with credentials.ini #
URL_API = config['minio']['url_api']
ACCES_KEY = config['minio']['acces_key']
SECRET_KEY = config['minio']['secret_key']
SECURE = config['minio']['secret']
TOKEN = config['minio']['token']

client = Minio(
    URL_API,
    access_key=ACCES_KEY,
    secret_key=SECRET_KEY,
    token=TOKEN,
    secure=SECURE
)

# get content with s3 select
with client.select_object_content(
        "my-bucket",
        "my-object.csv",
        SelectRequest(
            "SELECT * FROM S3Object",
            CSVInputSerialization(),
            CSVOutputSerialization(),
            request_progress=True,
        ),
) as result:
    for data in result.stream():
        print(data.decode())
    print(result.stats())
