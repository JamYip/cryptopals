# 小结

## Challenge 9

题目要求：实现PKCS#7填充

## Challenge 10

题目要求：实现 AES-CBC 加密

## Challenge 11

题目要求：区分ECB/CBC

条件：AES 密钥未知，部分明文可控，已知对应的密文。

```
 明文：(5-10 bytes random) + (your-input) + (5-10 bytes random)
```
解题思路：ECB明文块相同，则对应的密文块相同，输入3个相同的block，则密文必定存在两个相同的block。

假设前缀random bytes 为'aaaaaa'，后缀random bytes 为'bbbbbb'
输入 '0123456789abcdef0123456789abcdef0123456789abcdef'

明文block1：aaaaaa0123456789

明文block2：abcdef0123456789

明文block3：abcdef0123456789

明文block4：abcdef\0a\0a\0a\0a\0a\0a\0a\0a\0a\0a

明文 block2 等于明文 block3，所以密文 block2 也等于密文 block3

## Challenge 12

题目要求：获取 AES-ECB 的明文

条件：不知道明文，但可以在明文前加入我们想要的字符串，且可以获取加密后的密文。要获取未知的明文。

```
AES-128-ECB(your-string + unknown-string)
```

解题思路：

1. 计算出block的长度：当your-string长度等于block的长度时，此时的密文有如下特点：

```
AES-128-ECB(your-string + unknown-string, random-key) = AES-128-ECB(your-string) + AES-128-ECB(unknown-string) 
```
2. 逐一破解字符：
假设 block 长度为8，我们可以构造输入'AAAAAAA?'，其中 ? 是 0~128。使得下面两个密文的第一个block相等。

```
AES-128-ECB('AAAAAAA?' + unknown-string)
AES-128-ECB('AAAAAAA' + unknown-string)
```