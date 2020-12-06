# Docker Learning data and commands for setup and use
#### What is docker ?
##### Answer:
-    Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.
    
#### What is containarization ?
##### Answer:
-    Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels

#### Docker installation in ec2 ubuntu instance 

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
- `sudo apt-get update`
- `sudo apt-get install docker-ce `
- `apt-cache madison docker-ce`
```
sudo apt-get install docker-ce=5:18.09.1~3-0~ubuntu-xenial docker-ce-cli=5:18.09.1~3-0~ubuntu-xenial containerd.io
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```
- `sudo dpkg -i /path/to/package.deb`
- `sudo docker run hello-world`

- `sudo docker images`
- `sudo docker ps -a`
- `sudo docker version`
- `sudo docker info`
- `sudo docker run hello-world`
- `sudo docker pull alpine`
- `sudo docker pull ubuntu`
- particular version `sudo docker pull ubuntu:14.04`
- remove images `sudo docker rmi “image-id”`
- start stop container `sudo docker start <container>`, `sudo docker stop <container>`
- run a container `sudo docker run -it --name temp ubuntu:latest /bin/bash`
- exit from a container without killing it `ps -elf`
- Ctrl + P + Q
- stop all container `sudo docker stop $(docker ps -aq)`
- remove/delete all docker container `sudo docker rm $(docker  ps -aq)`

#### Swarm mode theory
- After install docker 
- Start swarm in 1st node `sudo docker swarm init --advertise-addr 35.173.134.200:2377`

### Dockerfile
```
FROM python
ADD my_script.py /home/ubuntu/my_docker_build/my_script.py
CMD [ "python", "/home/ubuntu/my_docker_build/my_script.py" ]

sudo docker build -t testpython/hello ./
sudo docker run testpython/hello
```