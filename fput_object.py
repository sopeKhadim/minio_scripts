from progress import Progress
from minio import Minio
from minio.error import MinioException
import configparser

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
# Put an object 'my-objectname' with contents from 'my-filepath'
try:
    result = client.fput_object('my-bucketname',
                                'my-objectname',
                                'my-filepath')
    print("created {0} object; etag: {1}, version-id: {2}".format(
        result.object_name,
        result.etag,
        result.version_id))

except MinioException as e:
    print(e)

# Put an object 'my-objectname-csv' with contents from
# 'my-filepath.csv' as 'application/csv'.
try:
    result = client.fput_object('my-bucketname',
                                'my-objectname-csv',
                                'my-filepath.csv',
                                content_type='application/csv'
                                )
    print("created {0} object; etag: {1}, version-id: {2}".format(
        result.object_name,
        result.etag,
        result.version_id)
    )

except MinioException as e:
    print(e)

# Put an object 'my-objectname-csv' with progress.
progress = Progress()
try:
    resut = client.fput_object('my-bucketname',
                               'my-objectname',
                               'my-filepath',
                               progress=progress)
    print("created {0} object; etag: {1}, version-id: {2}".format(
        result.object_name,
        result.etag,
        result.version_id)
    )

except MinioException as e:
    print(e)