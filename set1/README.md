# 小结

## Challenge 1

题目要求：hex to base64

## Challenge 2

题目要求：两个长度相等的hex进行异或运算

## Challenge 3

题目要求：破解 single-character XOR

已知：加密方式是异或加密，密钥长度1Byte

解题思路：暴力破解，遍历所有情况（密钥从0x00到0xff）。评估方法：明文对应词频表分值最高的密钥就是结果

## Challenge 4

题目要求：从文件中找出使用single-character XOR加密的密文

已知：密文长度 60-character strings（30 Byte）

解题思路：逐行遍历文件，选出词频分值最高的

## Challenge 5

题目要求：实现 repeating-key XOR

解题思路：对key进行扩展，使其长度等于明文，再一一对应进行异或运算

## Challenge 6

题目要求：破解 repeating-key XOR

已知：密文和加密方式

解题思路：https://www.anquanke.com/post/id/161171

## Challenge 7

题目要求：实现 128bit AES 加密，分组方式为 ECB，填充方式不做要求

解题思路：https://blog.csdn.net/qq_38289815/article/details/80900813

难点：列混淆的实现

## Challenge 8

题目要求：从文件中找出使用 128bit-AES-ECB 加密的密文

解题思路：使用ECB分组时，当明文有 128bit 相同时，密文也有 128 bit 相同。所以看哪一段密文，有重复的 128bit。（有局限，需要明文有重复的128bit）