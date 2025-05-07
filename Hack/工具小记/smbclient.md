# Smbclient 实战语句

- 列出 SMB 共享

```
    sudo smbclient -N -L \\\\10.10.10.10
```

- 连接到 SMB 共享

```
    sudo smbclient \\\\10.10.10.10\\enil
```