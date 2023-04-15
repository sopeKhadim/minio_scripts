
docker run      \
  -p 9000:9000  \
  -p 9090:9090  \
  --name "minio_server"                        \
  -v  ${HOME}/minio/data:/data:/mnt/data       \
  -v  ${HOME}/minio/conf:/etc/conf             \
  -e "MINIO_CONFIG_ENV_FILE=/etc/config.env"   \
  quay.io/minio/minio server /data --console-address ":9090"