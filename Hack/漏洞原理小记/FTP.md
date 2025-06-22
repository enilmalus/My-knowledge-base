# FTP 渗透小记

- 进入

```
    sudo ftp -p 10.10.10.16

    ls/dir
```

- 进入二进制

```
    binary
```

-  获取文件

```
    get test.txt
```

- 获取全部文件

```
	mget *.txt
```

- 关闭交互模式

```
	prompt
```