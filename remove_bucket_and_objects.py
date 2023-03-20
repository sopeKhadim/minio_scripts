#__author__='Djibril Mboup'
#__email__='limahin10@gmail.com'
from minio import Minio
from minio.error import MinioException
from minio.deleteobjects import DeleteObject
import configparser


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
# Remove an object.
try:
    client.remove_object('my-bucketname', 'my-objectname')
except MinioException as e:
    print(e)

# Remove list of objects.
errors = client.remove_objects(
    "my-bucketname",
    [
        DeleteObject("my-object1"),
        DeleteObject("my-object2"),
        DeleteObject("my-object3", "13f88b18-8dcd-4c83-88f2-8631fdb6250c"),
    ],
)
# Print errors
for error in errors:
    print("error occurred when deleting object", error)

# Remove a prefix recursively.
delete_object_list = map(
                        lambda x: DeleteObject(x.object_name),
                        client.list_objects("my-bucketname",
                                            "my/prefix/",
                                            recursive=True),)

errors = client.remove_objects("my-bucket",
                               delete_object_list)

# Print errors
for error in errors:
    print("error occurred when deleting object", error)

