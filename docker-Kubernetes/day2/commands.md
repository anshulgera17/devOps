#### commands

##### images

```bash
    > docker image ls
    > docker image pull hello-world
    > docker image rm hello-world

    > docker image build -t mywebsite .
    > docker image tag mywebsite <docker hub username>/mywebsite
    > docker login
    >
```

##### container

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

###### web hosting

```bash

    > cd /usr/share/nginx/html/
    > echo "<h1>welcome to my website</h1>" > index.html

    # OR

    > apt-get update
    > apt-get install vim
    > vim /usr/share/nginx/html/index.html
```

###### VSCode extensions

- https://marketplace.visualstudio.com/items?itemName=marquesmps.dockerfile-validator
- https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
- https://marketplace.visualstudio.com/items?itemName=jeff-hykin.better-dockerfile-syntax
