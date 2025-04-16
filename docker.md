### pull
docker pull centos
docker pull /Marcbark/centos:10.1.1

### run
docker run -d -t -p Whost:Dhost --name myname centos

### 查看运行中的容器
docker ps

### 查看占用
docker stats

### 启动
docker exec -it myname bash

### 停止容器
docker stop myname

### 重新开启容器
docker start myname