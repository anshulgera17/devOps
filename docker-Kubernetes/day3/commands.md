```bash

  > docker image pull openjdk:8
  > docker image build -t java-app .
  > docker container run -it --rm java-app
  > docker image prune
  > docker container run --rm -it --name app java-app-final
  > docker container run -itd --rm -p 8080:80 angular-app
  > docker container run -itd --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3006 mysql

  > docker volume ls
  > docker volume create myvolume

  > docker container run -itd --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -v myvolume:/var/lib/mysql mysql

  > docker container exec -it first bash

  > mysql -u root -p

```

```sql


  create database mydb;
  use mydb;
  create table person (id integer primary key auto_increment, name varchar(100), address varchar(100));
  insert into person (name, address) values ('person1', 'pune');
  insert into person (name, address) values ('person2', 'mumbai');
  insert into person (name, address) values ('person3', 'satara');
  select * from person;

```
