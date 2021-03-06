# Kubernetes

## Info
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

### Requirements for the local development
- Homebrew
- Hypervisor
- Minikube

## Setup (Macbook)
Minikube has the primary goals of being the best tool for local Kubernetes application development, and to support all Kubernetes features that fit.

### Kubectl vs Minikube
- Kubectl CLI = for configuring the minikube cluster
- Minikube CLI = for starting up/deleting the cluter

```bash
# install hypervisor, which creates a k8s image in vm (you can also select virtualbox or another vm tools)
brew install hyperkit

# kubectl is also pre-installed
brew install minikube
```
## Start
```bash
# download the kubernetes as a vm image and configure kubectl to use "minikube" cluster.

# docker is pre-installed and you don't need to install extra
minikube start --vm-driver=hyperkit

# check the node-cluster
kubectl get nodes
minikube status
minikube start

# reset
minikube stop
minikube delete --all
minikube start
minikube dashboard
```

## Kubectl

### Layer of Abstraction
- Deployment = blueprint to creating pods / configuration for deployment
- Deployment manages a replicaset
- ReplicaSet manages a Pod
- Pod is an abstraction of container

### Basics
```bash
- step1-nginx 
- step2-multi-service-mongodb
- step3-namespace-postgres
- step4-ingress-fastapi
- step5-k8s-dashboard
- step6-ingress-flask-postgresql
- step7-helm
```

### GKE
```bash
- step1 - Basics
- step2 - Managing Deployments Using Kubernetes Engine
- step3 - Continuous Delivery with Jenkins in Kubernetes Engine
- step4 - Wordpress
- Step5 - Nginx Ingress Controller
- step6 - Distributed Load Testing
- step7 - Version API 
- step8 - MongoDB in k8s with StatefulSets
```