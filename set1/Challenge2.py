'''Challenges   Set 1   Challenge 2    Fixed XOR'''
import struct
a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'
hex_a = a.decode('hex')
hex_b = b.decode('hex')
xor = []
for i,j in zip(hex_a, hex_b):
    xor.append(chr(ord(i) ^ ord(j)))
'''output: 746865206b696420646f6e277420706c6179'''
print(''.join(xor).encode('hex'))