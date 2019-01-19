'''Byte-at-a-time ECB decryption (Simple)'''
import random
import base64
from Crypto.Cipher import AES
import Challenge9


def generate_random(size):
    key=''
    for i in range(size):
        key = key + chr(random.randint(0,255))
    return key

def calc_block_size(cryptor, unkown_text):
    padding_unkown_text = Challenge9.padding_pkcs7(unkown_text, (len(unkown_text) // 16 + 1) * 16)
    crypt_text1 = cryptor.encrypt(padding_unkown_text)
    for i in range(1, 33):
        plain_text2 = generate_random(i) + unkown_text
        padding_plain_text2 = Challenge9.padding_pkcs7(plain_text2, (len(plain_text2) // 16 + 1) * 16)
        crypt_text2 = cryptor.encrypt(padding_plain_text2)
        if crypt_text2.find(crypt_text1) >= 0:
            return i

def calc_block(cryptor, block_size, unkown_text, buf, block_index):
    test_text = '0123456789abcdef'
    for offset in range(1, block_size + 1):
        test_text = test_text[0:block_size-offset]
        #print(test_text)
        padding_text = Challenge9.padding_pkcs7(test_text + unkown_text, (len(test_text + unkown_text) // block_size + 1) * block_size)
        crypt_text1 = cryptor.encrypt(padding_text)
        for i in range(128):
            padding_text2 = Challenge9.padding_pkcs7(test_text + buf + chr(i), (len(test_text + buf + chr(i)) // block_size + 1) * block_size)
            crypt_text2 = cryptor.encrypt(padding_text2)
            if crypt_text1[0 : block_size * block_index] == crypt_text2[0 : block_size * block_index]:
                buf = buf + chr(i)
                break
    return buf

def main():
    key = generate_random(16)
    cryptor = AES.new(key, AES.MODE_ECB)

    b64_unkown_text = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
    unkown_text = base64.b64decode(b64_unkown_text)

    block_size = calc_block_size(cryptor, unkown_text)
    print('Block size: %d', block_size)

    buf = ''
    buf_size = 0
    for i in range(1, 100):
        buf = calc_block(cryptor, block_size, unkown_text, buf, i)
        if len(buf) != buf_size:
            buf_size = len(buf)
        else:
            break
    print(buf)


if __name__ == '__main__':
    main()






