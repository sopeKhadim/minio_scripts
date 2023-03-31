import os
import configparser
from progress import Progress
from minio import Minio
from minio.error import MinioException

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

# Put a file with default content-type.
try:
    with open('my-testfile', 'rb') as file_data:
        file_stat = os.stat('my-testfile')
        result = client.put_object('my-bucketname',
                                   'my-objectname',
                                   file_data,
                                   file_stat.st_size)

        print("created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name,
            result.etag,
            result.version_id)
        )

except MinioException as e:
    print(e)

# Put a file with 'application/csv'
try:
    with open('my-testfile.csv', 'rb') as file_data:
        file_stat = os.stat('my-testfile.csv')
        result = client.put_object('my-bucketname',
                                   'my-objectname',
                                   file_data,
                                   file_stat.st_size,
                                   content_type='application/csv')

        print("created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name,
            result.etag,
            result.version_id))

except MinioException as e:
    print(e)

# Put a file with progress.
progress = Progress()
try:
    with open('my-testfile', 'rb') as file_data:
        file_stat = os.stat('my-testfile')
        result = client.put_object('my-bucketname',
                                   'my-objectname',
                                   file_data,
                                   file_stat.st_size,
                                   progress=progress)

        print("created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name,
            result.etag,
            result.version_id)
        )

except MinioException as e:
    print(e)
