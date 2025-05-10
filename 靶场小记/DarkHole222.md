
```

sudo nmap -sn 10.10.10.0/24
sudo nmap --min-rate 10000 -p- 10.10.10.9
sudo nmap -sT -sC -sV -p22,80 10.10.10.9 -oA nmap/Scan
sudo nmap --script=vuln -p22,80 10.10.10.9 -oA nmap/Script

sudo gobuster dir -u http://10.10.10.9 -w/usr/share/dirb/wordlists/common.txt 


cat /etc/passwd | grep "/bin/bash"

```