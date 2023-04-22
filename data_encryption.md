# Procedure d'encryption des données MinIO

## Pré-requis

- Installation [Hashicorp Vault](https://developer.hashicorp.com/vault)
- Installation [MinIO](https://min.io/docs/minio/linux/operations/install-deploy-manage/deploy-minio-single-node-single-drive.html#minio-snsd)
- Installation [MinIO KES](https://github.com/minio/kes)

## Prépartion
- Création de repertoires
```shell
mkdir -p $HOME/kes/{certs,config}  
mkdir -p $HOME/minio/{certs,config}  
mkdir -p $HOME/minio/data  
```
- Vérification des installs
```shell
minio  --version  
vault  --version  
kes  --version  
```
## Configuration Vault
- Démarrer Vault

```shell
vault server -dev  
...
Root Token: hvs.rCFo4tdgIdiq5NTRo6VzbBGi
```
- Ajouter les variables d'environnement **VAULT_ADDR** et **VAULT_TOKEN**
Le token doit etre remplacer par la valeur générée par vault par exemple :  

```shell
export VAULT_ADDR="http://127.0.0.1:8200"
export VAULT_TOKEN="hvs.rCFo4tdgIdiq5NTRjrVzbBGi"
```
- Créer un Vault secret engine path
```shell
vault secrets enable -path=kv kv
```
- Activer le approle pour prendre en charge le KES
```shell
vault auth enable approle
```
- Créer le fichier `kes-policy.hcl` et copier le contenue ci-dessous
```editorconfig
path "kv/data/*" {
    capabilities = [ "create", "read"]
}

path "kv/metadata/*" {
    capabilities = [ "list", "delete"]
}
```
- Appliquer les règles dèfini dans le fichier `kes-policy.hcl` à Vault.
```shell
vault policy write kes-policy kes-policy.hcl
```
- Créez un approle appelé kes-role et attribuez-lui la stratégie que nous avons créée à l'étape précédente.
```shell
vault write    auth/approle/role/kes-role policies=kes-policy
```

## Configuration de MinIO KES
- Génération des certificats TLS pour sécuriser la communication entre KES et Vault  

```shell
kes identity new kes_server \
  --key  $HOME/kes/certs/kes-server.key  \
  --cert $HOME/kes/certs/kes-server.cert  \
  --ip   "127.0.0.1"  \
  --dns  localhost
```
- Génération de certificats pour l'authentification de MinIO avec KES

```shell
kes identity new minio_server \
--key  $HOME/minio/certs/minio-kes.key  \
--cert $HOME/minio/certs/minio-kes.cert  \
--ip   "127.0.0.1"  \
--dns  localhost
```
- Définition des configs du KES dans le fichier `$HOME/kes/config/kes-config.yaml`
```yaml
address: 0.0.0.0:7373

admin:
  identity: disabled

tls:
  key:  $HOME/kes/certs/kes-server.key
  cert: $HOME/kes/certs/kes-server.cert

policy:
  minio:
    allow:
    - /v1/key/create/*   
    - /v1/key/generate/* # e.g. '/minio-'
    - /v1/key/decrypt/*
    identities:
    - MINIO_IDENTITY_HASH
keystore:
  vault:
    endpoint: http://localhost:8200
    engine: "kv/" # Replace with the path to the K/V Engine
    version: "v2" # Specify v1 or v2 depending on the version of the K/V Engine
    approle:
      id: "VAULTAPPID"     # Hashicorp Vault AppRole ID
      secret: "VAULTAPPSECRET" # Hashicorp Vault AppRole Secret ID
      retry: 15s
    status:
      ping: 10s
```
Modifier **MINIO_IDENTITY_HASH** avec la valeur de *identity* obtenue avec la commande  
```shell
kes identity of $HOME/minio/certs/minio-kes.cert
```

Remplacer **VAULTAPPID** par le id du *Approle ID* et **VAULTAPPSECRET** par le *secret ID*  

```shell
vault read     auth/approle/role/kes-role/role-id

Key        Value
---        -----
role_id    6924d20f-31b3-xxxx-6182-5fce1fd52d37

vault write -f auth/approle/role/kes-role/secret-id

Key                   Value
---                   -----
secret_id             0d6d8576-6a74-8f7f-xxx-785a5ec6fb3d
secret_id_accessor    16442cd9-8ba6-e730-042a-6ff756f2947f
secret_id_num_uses    0
secret_id_ttl         0s
```

## Configuration MinIO
- Ajouter les variables d'environnement MinIO dans les fichier `$HOME/minio/config/minio`

```shell
MINIO_KMS_KES_ENDPOINT=https://localhost:7373
MINIO_KMS_KES_CERT_FILE=$HOME/minio/certs/minio-kes.cert
MINIO_KMS_KES_KEY_FILE=$HOME/minio/certs/minio-kes.key
MINIO_KMS_KES_CAPATH=$HOME/kes/certs/kes-server.cert
MINIO_KMS_KES_KEY_NAME=minio-backend-default-key
```
- Démarrer KES 

```shell
sudo setcap cap_ipc_lock=+ep $(readlink -f $(which kes))
kes server --auth=off --config=/opt/kes/config/kes-config.yaml
```
- Démarrer MinIO Server
```shell
export MINIO_CONFIG_ENV_FILE=$HOME/minio/config/minio
minio server ~/minio/data --console-address :9090
```

## Encryption des données MinIO
