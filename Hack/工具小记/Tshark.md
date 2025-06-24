# Tshark 实战小记

查看流量

```
tshark -i eth0 -f "host 10.10.10.20"

tshark -i eth0 -f "host 10.10.10.20" -w flu.pcap

tshark -r flu.pcap

tshark -r flu.pcap -V
```

转换字符

```
tshark -r flu.pcap -T fields -e data | tr -d ' ' | xxd -r -p
```