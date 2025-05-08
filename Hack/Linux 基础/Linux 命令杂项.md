# Linux 命令杂项

-  修改主机名

```
    sudo hostnamectl set-hostname myname
```
-  grep 多层级搜索

```
    grep -lr "string"
```

-  连接 VPN

```
	sudo openvpn Marc.ovpn
```

-  显示通过 VPN 可访问的网络

```
    netstat -rn
```

-  ssh/ftp 远程连接

```
    ssh enil@10.10.10.10
    
    ftp 10.10.10.10
```