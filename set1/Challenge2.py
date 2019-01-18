'''Challenges   Set 1   Challenge 2    Fixed XOR'''
import struct

def hex_str_xor(hex_str1, hex_str2):
    hex1 = hex_str1.decode('hex')
    hex2 = hex_str2.decode('hex')
    xor = []
    for i,j in zip(hex1, hex2):
        xor.append(chr(ord(i) ^ ord(j)))
    return ''.join(xor).encode('hex')

def main():
    a = '1c0111001f010100061a024b53535009181c'
    b = '686974207468652062756c6c277320657965'
    '''output: 746865206b696420646f6e277420706c6179'''
    print(hex_str_xor(a, b))

if __name__ == '__main__':
    main()
