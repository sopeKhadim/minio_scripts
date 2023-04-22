# Procédure de notification de Bucket sur MySQL

## Création de base de données  MySQL

Créer un utilisateur miniouser et une base de données minio_db.

- mysql -u root -p
- CREATE user miniouser identified by 'pass123';
- CREATE database minio_db;
- GRANT ALL ON minio_db.* to miniouser;
- FLUSH privileges;

## Configuration de la notification d'un bucket

- Configuration avec mc

```
mc admin config set myminio notify_mysql:primary \   dsn_string="miniouser:minioadmin@tcp(localhost:3306)/minio_db" \
  table="bucketevents" \
  format="namespace" 
```

- Redémarrage de MinIO  
`mc admin service restart myminio`

- Vérification des configs  
 `mc event list ALIAS/BUCKET arn:minio:sqs::primary:mysql`

## Check des notifications après création ou manipulation d’objets

- `mysql -u root -p minio_db`
- `Select * from bucketevents;`

# Licence

UnLisense