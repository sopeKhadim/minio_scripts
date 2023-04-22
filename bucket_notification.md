# Procédure de notification de Bucket sur MySQL

## Création de base de données  MySQL

Créer un utilisateur miniouser et une base de données minio_db.
```shell
mysql -u root -p
```

```sql
mysql> CREATE USER miniouser identified BY 'pass123';
mysql> CREATE database minio_db;
mysql> GRANT ALL ON minio_db.* TO miniouser;
mysql> FLUSH PRIVILEGES;
```

## Configuration de la notification d'un bucket

- Configuration avec mc

```shell
mc admin config set myminio notify_mysql:primary \   
  dsn_string="miniouser:minioadmin@tcp(localhost:3306)/minio_db" \
  table="bucketevents" \
  format="namespace" 
```

- Redémarrage de MinIO
```shell
mc admin service restart myminio
```

- Vérification des configs  
```shell
mc event list ALIAS/BUCKET arn:minio:sqs::primary:mysql
```

## Check des notifications après création ou manipulation d’objets
```shell
mysql -u root -p minio_db
```

```sql
mysql> SELECT * FROM bucketevents;
```

# Licence

UnLisense