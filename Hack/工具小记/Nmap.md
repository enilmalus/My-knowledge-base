# Nmap 实战语句

- 主机发现

```
sudo nmap -sn [ip].0/24
```

- 探测端口

```
sudo nmap -sT --min-rate 10000 -p- 192.168.204.132 -oA nmap/port`

sudo nmap --min-rate 10000 -p- 10.10.10.13 | grep -E '^[0-9]+/tcp' | awk -F'/' '{printf "%s%s", sep, $1; sep=","}'
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

- 数据包分片扫描

```
sudo nmap -f -p- --min-rate 10000 10.10.10.20
```

- 源端口顺序扫描

```
sudo nmap --source-port 53 -p- --min-rate 10000 10.10.10.20
```

- 随机端口顺序扫描

```
sudo nmap -r -p- --min-rate 10000 10.10.10.20
```

- TCP Windows 扫描

```
sudo nmap --scanflags URGPSHFIN -p- --min-rate 10000 10.10.10.20
```

- 慢速扫描

```
sudo nmap -T2 -p- 10.10.10.20
```

