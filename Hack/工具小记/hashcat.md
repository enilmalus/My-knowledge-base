# Hashcat 实战语句

-  MD5

```
sudo hashcat -m 0 -a 0 hash/hash.lst /usr/share/wordlists/rockyou.txt
```

- 查看破解过的 hash

```
sudo hashcat -m 0 --show hash/hash.lst
```

- 7z

```
sudo hashcat -m 11600 -a 0 7z_hash.txt /usr/share/wordlists/rockyou.txt
```

## -m 参数对照表

|类型|参数|
|---|---|
|MD5|0|
|SHA1|100|
