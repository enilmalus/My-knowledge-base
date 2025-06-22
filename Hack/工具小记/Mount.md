# mount 实战语句小记

- 检查共享目录

```
showmount -e 10.10.10.13
```

- 连接共享目录

```
sudo mount -t nfs 10.10.10.13:/home/karl attact
```