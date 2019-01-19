#coding=utf-8
'''
Challenges   Set 1   Challenge 6    Break repeating-key XOR

原理：这篇blog解析得很详细：https://www.anquanke.com/post/id/161171'''
import base64
import Challenge3
import Challenge5
'''计算汉明距离'''
def hamming_dis(str1, str2):
    dis = 0
    for i,j in zip(str1, str2):
        dis = dis + bin(ord(i) ^ ord(j)).count('1')
    return dis

def cal_distance(text, key_size):
    distance = []
    str1 = text[0 : key_size]
    for i in range(1, 5):
        str2 = text[(i + 1) * key_size : (i + 2) * key_size]
        distance.append(hamming_dis(str1, str2))
    return sum(distance) / key_size

def xor(crypto, key):
    buf = []
    for ch in crypto:
        buf.append(chr(ord(ch) ^ ord(key)))
    return ''.join(buf)

def main():
    with open('./6.txt', 'r') as f:
        data = f.read()
        hex_text = base64.b64decode(data)

        # 汉明距离最小的最有可能是key size
        # 此处假定汉明最小的就是key size
        distance_list = {}
        for key_size in range(3, 41):
            distance_list[key_size] = cal_distance(hex_text, key_size)
        key_size = min(distance_list, key = distance_list.get)
        print('key size is %d', key_size)

    key = ''
    for i in range(key_size):
        score_list = {}
        for ch in range(127):
            plain_text = xor(hex_text[i::29], chr(ch))
            score_list[ch] = Challenge3.calc_score(plain_text)
        plain_ch = max(score_list, key = score_list.get)
        key = key + chr(plain_ch)
    print('key is ==> ' + key)
    print('====================================================')
    print(Challenge5.enc_repeat_xor(hex_text, key).decode('hex'))

if __name__ == '__main__':
    main()