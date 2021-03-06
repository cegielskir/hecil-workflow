# hecil-workflow

## Building images
### Worker container
```
docker build -t hecil-worker:0.1 hecil-worker/
```
### Data contaier
```
docker build --build-arg NUMBER_OF_CONTIGS=100 --build-arg LENGTH_OF_CONTIGS=10 --build-arg NUMBER_OF_SPLITS=10  -t hecil-data-container:0.1 hecil-data-container/
```

## Configure Hyperflow Kubernetes charts
```
git clone https://github.com/hyperflow-wms/hyperflow-k8s-deployment.git
cd hyperflow-k8s-deployment
git apply ../k8s.patch
```
## Running the workflow

### Deploying to cluster
Follow [deployment instructions](https://github.com/hyperflow-wms/hyperflow-k8s-deployment#running-the-workflow) from Hyperflow repository. Mind the typo in the thrid line of the resource installation code block - the appropriate file is `hyperflow-engine.yaml`, not `hyperflow-engine.yml`.

### Deploying with minikube
For running within minikube env instead:
```
helm install nfs-server charts/nfs-server --values values/minikube/nfs-server.yml
helm install redis charts/redis --values values/minikube/redis.yml
helm install hyperflow-endinge charts/hyperflow-engine --values values/minikube/hyperflow-engine.yml
```
