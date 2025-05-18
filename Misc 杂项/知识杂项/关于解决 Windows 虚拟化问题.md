# 关于解决 Windows 虚拟化问题

## Vmware 启动虚拟机时报错

![[Pasted image 20250516194514.png]]

去 [Microsoft 官网](https://www.microsoft.com/en-us/download/details.aspx?id=53337)下载并解压

管理员打开 Powershell 进入该目录

![[Pasted image 20250516194751.png]]

运行

```
.\DG_Readiness_Tool_v3.6.ps1 -Disable
```

如果报错则继续，没保存则重启后按 F3 继续

![[Pasted image 20250516194906.png]]

报错：

```
set-ExecutionPolicy RemoteSigned
```

```
get-ExecutionPolicy
```

重启按 F3

在启用或关闭Windows功能中,关闭如下几个选项

![[Pasted image 20250516195103.png]]

![[Pasted image 20250516195112.png]]

## 开启基于虚拟化的安全性

```
.\DG_Readiness_Tool_v3.6.ps1 -Enable -HVCI -CG
```

## 验证

```
.\DG_Readiness_Tool_v3.6.ps1 -Ready
```


# 不支持嵌套虚拟化

![[Pasted image 20250516200435.png]]

Powershell(管理员) 

```
bcdedit /set hypervisorlaunchtype off
```

重启