### 修改主机名
    sudo hostnamectl set-hostname myname


### grep多层级搜索

    grep -lr "string"

### 连接vpn

sudo openvpn Marc.ovpn
##### 显示通过vpn可访问的网络
    netstat -rn

### ssh/ftp远程连接

    ssh enil@10.10.10.10
    ftp 10.10.10.10