# Gobuster 实战语句

-  gobuster 爆破

```
sudo gobuster dir -u http://10.10.10.10/ -w /usr/share/dirb/wordlists/commom.txt
````

-  gobuster 子域名扫描

```
sudo gobuster dns -d marcbark.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```

-  gobuster 指定特定的后缀

```
sudo gobuster dir -u http://10.10.10.18/secret/ -w /usr/share/dirb/wordlists/common.txt -x html,txt,php
```

- gobuster 常用搜索

```
sudo gobuster dir -u http://10.10.10.31 -w /usr/share/wordlists/dirb/common.txt -x php,php.bak,jsp.zip,html
```