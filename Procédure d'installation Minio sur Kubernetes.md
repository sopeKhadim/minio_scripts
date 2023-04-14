# Procedure d'installation Minio sur Kubernetes

## Creation Single Node Single Drive Cluster sur Minikube

### Pré-requis

- Installer Kubernetes ou Minikube en local

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
- Récuperer le fichier de deploiement minio-dev.yaml
  - `curl https://raw.githubusercontent.com/minio/docs/master/source/extra/examples/minio-dev.yaml -O`
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


## Creation Multitenant cluster Cluster sur Kubernetes

### Pré-requis

- Installer Kubernetes ou Minikube en local
- krew
- helm  (optionel)

### Creation du cluster avec minikube

- Demarrer Minikube cluster
  - `minikube start -p cluster1`
- Vérification des pods et configs
  - `kubectl get po -A`
  - `kubectl get pod kube-controller-manager-<replace_with_cluster_name>   -n kube-system -o yaml
- Minikube Dashboard
  - `minikube dashboard`

### Installation et deploiment

- Installation de MinIO Operator plugin avec krew
  - `kubectl krew search minio`
  - `kubectl krew update`
  - `kubectl krew install minio`
  - `kubectl minio version`
- Générer un Manifest pour le déploiement
   `kubectl minio init --cluster-domain cluster.local --output > minio-init.yaml`
- Deployer MinIO Operator
  - `kubectl apply -f minio-init.yaml`
- Vérification des ressources
  - `kubectl get ns` 
  - `kubectl get all -n minio-operator
- Démarrer un forward proxy pour acceder à MinIO Operator UI Console
  - `kubectel minio proxy`
  - Copier le JWT généré pour acceder au Console

### Création de tenant

- Création d'un namespace
  - `kubectl create namespace storage`
- Télécharger le fichier local-path-provisioner.yml pour la création et le montage de de volume
  - `curl https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.24/deploy/local-path-storage.yaml`
- Déployer le fichier yaml
  - `kubectl apply -f local-path-provisioner.yml`
- Verification du pv et du pvc
  - `kubectl get pv`
  - `kubectl get pvc - A`
- Créer un tenant dans MinIO Operator avec le namespace storage et le storage class local-path
  - Configuerer les ressources en tenant compte du erasure coding
- Verifier les ressources
  - `kubectl get pv`
  - `kubectl get pvc -n storage`
