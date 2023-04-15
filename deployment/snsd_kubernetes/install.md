# Procedure d'installation Minio sur Kubernetes

## Creation Single Node Single Drive Cluster sur Minikube

### Prérequis

- Installer Minikube en local
- Installer Git
### Creation du cluster avec minikube

- Demarrer Minikube cluster
  - `minikube start -p cluster1`
- Vérification
  - `kubectl get po -A`
- Minikube Dashboard
  - `minikube dashboard`

### Déployement MinIO

- Créer un volume dans dans le repertire /mnt/
  - `mkdir -m 777 /mnt/data
- Cloner le code source git.
  - `git clone https://github.com/sopeKhadim/minio_scripts.git`
- Se déplacer dans le dossier ou se trouve le fichier minio-dev.yaml
  - `cd minio_scripts/deployment/snsd_kubernetes`
- Ouvrir le fichier minio-dev
  - Remplacer `kubealpha.local` avec le nom de votre cluster `cluster1`
  - Remplacer `/mnt/disk1/data` avec `/mnt/data`

- Deployer le fichier minio-dev.yml
  - `kubectl apply -f minio-dev.yml`
- Verification des pods crées
  - `kubectl get pods -n minio-dev`
  - `kubectl describe pod/minio -n minio-dev`
  - `kubectl logs pod/minio -n minio-dev`

### Démarrer MinIO Console

- Activer le forward proxy
  - `kubectl port-forward pod/minio 9000 9090 -n minio-dev`
- Acceder MinIO UI Console sur l'url http://127.0.0.1:9090.
- Les credentials par défaut sont `minioadmin | minioadmin`


## Licence
@UnLicense