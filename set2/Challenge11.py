'''Challenges   Set 2   Challenge 11    An ECB/CBC detection oracle'''

import random
import base64
from Crypto.Cipher import AES
import Challenge9

def generate_random(size):
    key=''
    for i in range(size):
        key = key + chr(random.randint(0,255))
    return key


def main():
    key = generate_random(16)
    iv = generate_random(16)

    r = random.randint(0,1)
    print('random: %d', r)
    if r == 0:
        cryptor = AES.new(key, AES.MODE_CBC, iv)
    else:
        cryptor = AES.new(key, AES.MODE_ECB)


    text = 'fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
    plain_text = generate_random(random.randint(5,10)) + text + generate_random(random.randint(5,10))
    padding_text = Challenge9.padding_pkcs7(plain_text, (len(plain_text) // 16 + 1) * 16)
    crypt_text = cryptor.encrypt(padding_text)

    print('%x', crypt_text)
    print('key: ' + base64.b64encode(key))
    print('iv: ' + base64.b64encode(iv))
    if crypt_text[16:32].find(crypt_text[32:48]) >= 0:
        print 'ECB'
    else:
        print 'CBC'

if __name__ == '__main__':
    main()