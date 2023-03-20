from minio import Minio
from minio.error import MinioException
import configparser
import subprocess

config = configparser.ConfigParser()
config.read('credentials.ini')

# Set the credentials with credentials.ini ####
URL_API = config['minio']['url_api']
ACCES_KEY = config['minio']['acces_key']
SECRET_KEY = config['minio']['secret_key']
SECURE = config['minio']['secret']

client = Minio(
    URL_API,
    access_key=ACCES_KEY,
    secret_key=SECRET_KEY,
    secure=SECURE
)
# Get a full object into a file
try:
    data = client.get_object('my-bucket',
                             'my-object')

    with open('my-testfile', 'wb') as file_data:
        for d in data.stream(32*1024):
            file_data.write(d)

except MinioException as e:
    print(e)

# Get data from an object, Read data from response..
try:
    response = client.get_object("my-bucket",
                                 "my-object")
    proc = subprocess.Popen(["less"], stdin=subprocess.PIPE)
    # this would load the total file into memory, if the file is big,
    # we might meet some error, but don't worry for now.
    proc.communicate(response.read())

finally:
    response.close()
    response.release_conn()