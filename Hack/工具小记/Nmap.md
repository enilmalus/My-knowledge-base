# Nmap 实战语句

- 主机发现

```
	sudo nmap -sn [ip].0/24
```

- 探测端口

```
	sudo nmap -sT --min-rate 10000 -p- 192.168.204.132 -oA nmap/port`
```

>	-oA xx（以全格式输出到 txt ）

- 基本信息探测

```
	sudo nmap -sT -sC -sV -O -p22,80 192.168.204.132 -oA nmap/AAA
````


- UDP 扫描

```
sudo nmap -sU --top-ports 20 192.168.204.132 -oA nmap/UDP
````

- 脚本扫描 

```
sudo nmap --script=vuln -p22,80,139,901,8080,10000 192.168.204.132 -oA nmap/script
````

