# Single-Node Mult-Drives (SNMD)

## Prérequis :
- Installation Docker ou Docker Desktop
- Installation Git

## Installation et déploiement:
Cloner le code source git.  
- `git clone https://github.com/sopeKhadim/minio_scripts.git`

Se déplacer sur le répertoire minio_scripts/deployment/snmd_docker  
- `cd minio_scripts/deployment/snmd_docker`  

Exécuter la commande suivant :  
- `docker compose up`  

Démarrer MinIO UI Console sur http://localhost:9090 avec les credentials minioadmin|minioadmin

Inspecter Docker  
- `docker ps`
- `docker logs -f --until=2s minio`


## Licence
@UnLicense