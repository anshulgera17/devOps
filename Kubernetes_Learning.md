# Kubernetes learning and command to use 
- Q1. What is Kubernetes ?
#### Answer
- Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. The name Kubernetes originates from Greek, meaning helmsman or pilot.

- Pods
- Network
- Etcd
- Kubelet - deamon for kubernetes
- Kubectl
- Kubeadm - bootstraper for kubernetes
- Kucectl get pods --all-namespaces
- Kubectl get nodes
- Master
- Etcd
- Api server
- Scheduler 
- Controller manager
- Node (similar to minions) previously called them minions, node contains (kubelet, kubeproxy, Pod(container))
- Proxy
- Kubelet
- Container runtime

#### Kubernetes Architecture ?
#### Answer:
- Kube Apiserver
- Etcd
- Kube Schedular
- Cloud controller manager
- kube controller manager

#### Kubernetes Objects 
#### Answer:
- Nodes
- Pods
- Deployments
- Services
- Config Maps

#### Installation commands for ubuntu 18.04
- https://phoenixnap.com/kb/install-kubernetes-on-ubuntu
- if face issue follow this page for docker issue https://itsfoss.com/could-not-get-lock-error/ 

#### Practice
```
kubectl create -f nginx.yaml
kubectl get pods
kubectl describe pods
kubectl delete pod pod-name
kubectl get nodes (check nodes status from master)
kubectl describe node nodename
kubectl get deployments
kubectl describe deployment nginx
kubectl get deployment nginx-deployment -o yaml
kubectl set image deployment/nginx-deployment nginx=nginx:1.8 (for update the image )
kubectl create -f nginx-deployment.yaml
kubectl get pods -l app=nginx -o wide
kubectl set image deployment nginx-deployment nginx=nginx:1.8
kubectl apply -f nginx-deployment.yaml
kubectl rollout undo deployment/nginx-deployment 
kubectl rollout status deployment nginx-deployment
kubectl rollout history deployment nginx-deployment
kubectl rollout undo deployment nginx-deployment --to-revision=x
kubectl delete -f nginx-deployment.yaml
```