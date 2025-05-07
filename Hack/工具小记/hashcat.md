# Hashcat 实战语句

-  MD5

```
	sudo hashcat -m 0 -a 0 hash.lst /usr/share/wordlists/rockyou.txt
```

## -m 参数对照表

|类型|参数|
|---|---|
|MD5|0|
|SHA1|100|
