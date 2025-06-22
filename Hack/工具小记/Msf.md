# Msf 使用小记

- 创建 600 字节缓冲区

```
msf-pattern_crate -l 600
```

- 确定字节

```
msf-pattern_offset -l 600 -q 35724134
```

- jum esp

```
msf-nasm_shell

jmp esp
```