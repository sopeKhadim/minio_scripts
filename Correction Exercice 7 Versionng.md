# Correction Exercice Versionng

## Créer un bucket mybucket

- MinIO Console (Voir TP précedent)
- mc commande

```shell
      mc alias set myminio http://localhost:9090 minioadmin minioadmin
      mc mb myminio/my-bucket
```

## Activer le versioning

- MinIO Console : On doit l'activer lors de la création du bucket
- MinIO CLI :

```shell
    mc version enable myminio/my-bucket
```

## Créer et Copie le fichier file.txt dans my-bucket

```shell
  echo "Hello World" > file.txt
  mc cp file.txt myminio/my-bucket
```

## Modifier le fichier

```shell
  echo –e "A new record added" >>  file.txt
```

## Recopier à nouveau le fichier

```shell
  mc cp file.txt myminio/my-bucket
```

## Vérifier le contenue avec mc ls puis avec mc ls –versions.

```shell
  mc ls myminio/my-bucket
  mc ls -- myminio/my-bucket ## nous avons deux versions du fichiers file.txt v1 et v2
```
  
## Supprimer le fichier avec mc rm

```shell
  mc rm myminio/my-bucket/file.txt
```

## Vérifier mc ls --versions

```shell
  mc ls --versions myminio/my-bucket/ ## Nous avons deux version avec v2 marquer par un O-bit DeleteMarker
```

## Supprimer définitivement le fichier

```shell
  mc rm --version-id 4bxxxxxxxxxxxxxxxxxxf # uid-version
```

## check si le fichier a été Supprimer

```shell
  mc ls --versions
```