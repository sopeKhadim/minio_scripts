# Procedure d'installation Minio Multi-tenant Cluster sur Kubernetes

- **Note** : Installation à valider

### Prérequis

- Installer Kubernetes ou Minikube en local
- krew
- helm  (optionel)

### Creation du cluster avec Minikube

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

## Licence
@UnLicense