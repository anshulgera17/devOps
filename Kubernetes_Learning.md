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
- Node
- Proxy
- Kubelet
- Container runtime

#### Installation commands
```
sudo su 
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
modprobe br_netfilter
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce
```
```
cat << EOF > /etc/yum.repos.d/kubernetes.repo  
[kubernetes]  
name=Kubernetes  
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64  
enabled=1  
gpgcheck=0  
repo_gpgcheck=0  
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg  
 https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg  
 
EOF 
```
```
yum install -y kubelet kubeadm kubectl

systemctl enable docker
systemctl enable kubelet
systemctl start docker
systemctl start kubelet
docker info | grep -i cgroup
```
```
sed -i 's/cgroup-driver=systemd/cgroup-driver=cgroupfs/g'  /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

systemctl daemon-reload
systemctl restart kubelet

kubeadm init --pod-network-cidr=10.244.0.0/16
```
- Exit from sudo then run below 3 commands
```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```
```
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl get pods -—all-namespaces
kubectl get nodes
kubectl create deployment nginx --image=nginx
kubectl get pods
kubectl scale deployment nginx --replicas=4
kubectl get pods
```
```
kubectl get namespaces
kubectl create namespace podexample 
kubectl create -f ./pod-example.yaml
kubectl get pods
kubectl exec -it container_name /bin/bash → this will send you the root folder to the container.
cat /etc/resolv.conf
kubectl get all --all-namespaces -o wide
```
#### ReplicaSets
```
kubectl describe rs/frontend
kubectl scale rs/frontend --replicas=4 --> for create replicas of the pods
kubectl delete rs/frontend
```

```
kubectl create -f ./filename.yml
kubectl describe service name_of_service
kubectl scale service_name --replicas=4
```

##### This lesson covers how to install Kubernetes on CentOS 7. Below, you will find a list of the commands used in this lesson.
- https://www.youtube.com/watch?v=UWg3ORRRF60  → refer video for install in ubuntu instance
- The first thing that we are going to do is use SSH to log in to all machines. Once we have logged in, we need to elevate privileges using sudo `sudo su`
- Disable SELinux
```
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g'
/etc/sysconfig/selinux
```

- Enable the br_netfilter module for cluster communication
```
modprobe br_netfilter
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
```
- Disable swap to prevent memory allocation issues
```
Swapoff -a
 Vim /etc/fstab.  ->  Comment out the swap line
```
- Install Docker CE.
- Install the Docker prerequisites `yum install -y yum-utils device-mapper-persistent-data lvm2`
- Add the Docker repo and install Docker.
- `yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`
- `yum install -y docker-ce`

- Add the Kubernetes repo
```
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
 [kubernetes]
 name=Kubernetes
 baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
 enabled=1
 gpgcheck=0
 repo_gpgcheck=0
 gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
         https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
 EOF
```
- Install Kubernetes.
- `yum install -y kubelet kubeadm kubectl`

- Reboot
- Enable and start Docker and Kubernetes.
```
systemctl enable docker
systemctl enable kubelet
systemctl start docker
systemctl start kubelet
```
- Check the group Docker is running in `docker info | grep -i cgroup`

- Set Kubernetes to run in the same group 
- `sed -i 's/cgroup-driver=systemd/cgroup-driver=cgroupfs/g' /etc/systemd/system/kubelet.service.d/10-kubeadm.conf`

- Reload systemd for the changes to take effect, and then restart Kubernetes
```
systemctl daemon-reload
systemctl restart kubelet
```

- *Note: Complete the following section on the MASTER ONLY!
- Initialize the cluster using the IP range for Flannel.
- `kubeadm init --pod-network-cidr=10.244.0.0/16`

- Copy the kubeadmin join command.
- Deploy Flannel.
- `kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml`


- Exit sudo and run the following:
```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

- Check the cluster state `Kubectl get pods —all-namespaces`
- Note: Complete the following steps on the NODES ONLY!
- Run the join command that you copied earlier, then check your nodes from the master `kubectl get nodes`