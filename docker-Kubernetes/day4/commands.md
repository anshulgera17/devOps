```bash

  > docker container run -itd --name myapp -p 8080:80 -v /Volumes/Data/today/docker/app1/:/usr/local/apache2/htdocs/ httpd

```

```bash

  > docker network ls
  > docker network inspect bridge
  > docker network create --subnet 192.168.1.0/24 mybridge
  > docker network create --subnet 192.168.1.0/24 --driver bridge mybridge
  > docker network rm mybridge
  > docker container run -itd --name c3 --network mybridge alpine
  > docker network disconnect bridge c1
  > docker network connect mybridge c1
  > docker network connect mybridge c2

  > docker container run --name httpd-1 --network host -itd httpd
```
