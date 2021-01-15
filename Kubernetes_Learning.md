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


