
本地主机发现：`sudo nmap -sn [ip].0/24`
探测主机：`sudo nmap -sT --min-rate 10000 -p- 192.168.204.132 -oA nmap/port`
-oA xx(以全格式输出到txt)

提取nmap扫描出的端口：`grep "open" nmap/TCP.nmap | awk -F '/' '{print $1}' | paste -sd ","`

nmap最重扫描：`sudo nmap -sT -sC -sV -O -p22,80,139,901,8080,10000 192.168.204.132 -oA nmap/AAA`

UDP扫描：`sudo nmap -sU --top-ports 20 192.168.204.132 -oA nmap/UDP`

默认脚本扫描： `sudo nmap --script=vuln -p22,80,139,901,8080,10000 192.168.204.132 -oA nmap/script`

whois脚本扫描：``sudo nmap --script=whois-domain 192.168.204.132 -oA nmap/whoifs``

穿透防火墙扫描：`sudo nmap -Pn -A [ip]
`
-sO：IP扫描
-sI：空闲扫描
-sS：TCP/SYN扫描
-p：指定端口号扫描
-v：显示扫描过程
-F：快速扫描
-Pn：禁止ping后扫描：跳过主机发现的过程进行端口扫描
-A：全面的系统扫描
-sT：TCP扫描
-sU：UDP扫描
-sV：扫描系统和程序版本号检测
–script=vuln：漏洞扫描
-n：禁止反向域名解析
-R：反向域名解析
-6：启动IPV6扫描
-sP：使用Ping扫描
-PO：不使用Ping扫描
-sN；-sF；-sX：隐蔽扫描
-T0；-T1：慢速扫描，躲避IDS与WAF
-T2：稍慢速扫描
-T3：默认
-T4：快速扫描
-T5：极速扫描

Opend：端口开启
Closed：端口关闭
Filtered：端口未被过滤，数据没有到达主机，返回结果为空，数据被防火墙拦截
UnFiltered：未被过滤，数据到达主机，但是不能识别端口当前状态
Open|filtered：开放或被过滤，端口没有返回值，主要发生在UDP、IP、FIN、NULL和Xmas扫描中
Closed|filtered：关闭或被过滤，只发生在IP、ID、idle扫描

常见端口号：

端口号 端口说明 攻击反向
80/443/8080 常见web服务端口 web攻击、爆破、对应服务器版本漏洞
7001/7002 weblogic控制台 Java反序列化、弱口令
8080/8089 Jboss/Resin?/Jenkins 反序列化、弱口令
9090 WebShphere 控制器 Java反序列化、弱口令
4848 GlassFish控制台 弱口令
1352 Lotus domino 邮件服务 弱口令、信息泄露、爆破
10000 Webmin-Web 控制面板 弱口令
