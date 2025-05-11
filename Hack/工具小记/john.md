# John 实战语句

- 破解 hash

```
sudo john hash/hash.lst --wordlist=/usr/share/wordlists/rockyou.txt hash/users.lst
```

- 破解 id_rsa

```
/usr/share/john/ssh2john.py hash/id_rsa > crack.txt  

john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa     
```

