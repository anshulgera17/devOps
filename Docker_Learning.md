# Docker Learning data and commands for setup and use

## What is docker ?

- Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.(solomon hykes)
golang is used to create docker

## What is containarization ?

- Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels
- Leightweight
- containers will be treated as processes
- process level isolation
- less secure
- start very fast 
- pre-built containers
- easy to create and destroy(immutable)
- create in seconds

## Explain docker architecture ?

- REST API + dockerd (namespaces + libcontainer + control groups (cgroups) )

## Layer based approach

- Union file system (UnionFS)
- UFS having AUFS, Btrfs, VFS and devicemapper
- Layered file system contains: writtable layer + (run application + install JVM+ copy source + Manifest)

## what are the docker objects ?

- Images
- Containers
- Network
- Volumes
- Registry
- Service

## Modes in Docker

- Attached mode (container will also exitted, after exit)
- Dettached mode

## Dockerfile

- FROM
- ENV
- RUN
- CMD
- EXPOSE
- WORKDIR
- ADD
- COPY
- LABEL
- MAINTAINER
- ENTRYPOINT

## what is port forwarding

- sending server request to container port is port forwarding we can achieve by `docker container run -itd --name nginx -p 8080:80 nginx` p option
- port forwarding or port mapping is an application of network address translation that redirects a communication request from one address and port number combination to another while the packets are traversing a network gateway, such as a router or firewall

## Docker installation in ec2 ubuntu instance

- Go to this link and run commands:-
- `https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository`
- Or 
- `sudo apt-get remove docker docker-engine docker.io`
- `sudo apt-get update`
```
    sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
    
```

- `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
- `sudo apt-key fingerprint 0EBFCD88`

```
   sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

- `apt-get update`
- `apt-get install docker-ce`
- `apt-cache madison docker-ce`

```

sudo apt-get install docker-ce=5:18.09.1~3-0~ubuntu-xenial docker-ce-cli=5:18.09.1~3-0~ubuntu-xenial containerd.io
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

- `sudo groupadd docker` create docker group
- `sudo usermod -aG docker $USER` add your user to docker group

- `docker version`
- `docker info`
- `docker pull ubuntu:14.04` particular version 
- `docker rmi “image-id”` remove images 
- `ps -elf` exit from a container without killing it 
- Ctrl + P + Q
- `docker stop $(docker ps -aq)` stop all container 
- `docker rm $(docker  ps -aq)`remove/delete all docker container 

## images

```bash
    > docker image ls
    > docker image pull hello-world
    > docker image rm hello-world

    > docker image build -t mywebsite .
    > docker image tag mywebsite <docker hub username>/mywebsite
    > docker login
```

## container

```bash
    > docker container create hello-world
    > docker container start <container id/name>
    > docker container stop <container id/name>

    > docker container ls
    > docker container ls -a

    > docker container rm <container id/name>

    > docker container run hello-world
    > docker container run --name mycontainer hello-world
    > docker container run --name mycontainer --rm hello-world

    > docker container run --name ubuntu --rm ubuntu date
    > docker container run --name ubuntu -it ubuntu
    > docker container run --name ubuntu -itd ubuntu
    > docker container start ubuntu
    > docker container attach ubuntu
    > docker container exec ubuntu ls -l
    > docker container exec -it ubuntu bash

    > docker container run -itd --name mysql -e MYSQL_ROOT_PASSWORD=root  mysql

    > docker container run -itd --name nginx nginx

    > docker container inspect nginx
    > docker container run -itd --name nginx -p 8080:80 nginx
```

## Swarm mode theory

- After install docker 
- Start swarm in 1st node `sudo docker swarm init --advertise-addr 35.173.134.200:2377`

## Dockerfile

```
FROM python
ADD my_script.py /home/ubuntu/my_docker_build/my_script.py
CMD [ "python", "/home/ubuntu/my_docker_build/my_script.py" ]

sudo docker build -t testpython/hello ./
sudo docker run testpython/hello
```