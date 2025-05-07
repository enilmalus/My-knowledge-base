# Gobuster 实战语句

-  gobuster 爆破

```
	sudo gobuster dir -u http://10.10.10.10/ -w /usr/share/dirb/wordlists/commom.txt
````

-  gobuster 子域名扫描

```
	sudo gobuster dns -d marcbark.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```