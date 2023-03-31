from minio import Minio
from minio.error import MinioException
from minio.sse import SseCustomerKey
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

# download a full object
try:
    client.fget_object('my-bucketname', 'my-objectname', 'filepath')
except MinioException as e:
    print(e)

# Download data of an SSE-C encrypted object.
# Try this if you are an SSE Key
try:
    client.fget_object("my-bucket", "my-object", "my-filename",
                       ssec=SseCustomerKey(b"32byteslongsecretkeymustprovided"),
                       )
except MinioException as e:
    print(e)
