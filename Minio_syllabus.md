# MINIO : Multi-Cloud Object Storage

## PLAN

- Session 1 : Les Fondamentaux
- Session 3 : MinIO Deploiemnet
- Session 4 : de MINIO
- Session 5 : MinIO Administration
---
1. Session 1 : Les Fondamentaux
   - File Storage vs Block Storage
   - Object ou BLOB
   - Qu'est ce qu'un bucket
   - Object Storage
   - MinIO Object Storage
     - Architecture
     - Scalabilité
     - Compatibilité avec s3
     - Native Cloud
     - Les Composants de MinIO

2. Session 2 : Deploiement de MinIO
    - Topologie de déploiment
    - Single-Node Single-Drive (SNSD or “Standalone”)
    - Single-Node Multi-Drive (SNMD or “Standalone Multi-Drive”)
    - Multi-Node Multi-Drive (MNMD or “Distributed”)
    - Déploiement Multi-tenant sur un cluster Kubernetes

3. Session 3 : Minio Client
   - Minio CLI 
     - Création et Gestion des buckets S3
     - Manipulation des objets PUT/GET/DELETE 
     - Listing, Copying, Affichage, Recherche d’objets 
     - Mirroring des buckets
   - Minio SDK 
     - Installation Python SDK 
     - Gestion des buckets S3 
     - Manipulation des objets PUT/GET/DELETE 
     - Listing, copying, affichage, Recherche d’objets 
     - Amazon S3 API (boto3)
     
4. Session 4 : Administration 
    - MinIO Erasure Coding
    - Bucket Notification
    - Versioning 
    - Verrouillage et Rétention d’objets
    - Identity & Access Management (IAM)
    - Replications & Backups
    - Sécurisation TLS
    - Encryption des Données