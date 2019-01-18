'''Challenges   Set 1   Challenge 3    Single-byte XOR cipher'''

# http://www.data-compression.com/english.html
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

'''
crypto is a hex string, without 0x. key is a char
'''
def denc_xor(crypto, key):
    hex_data = crypto.decode('hex')
    buf = []
    for ch in hex_data:
        buf.append(chr(ord(ch) ^ ord(key)))
    return ''.join(buf)

def calc_score(string):
    score = 0
    for c in string:
        c = c.lower()
        if c in CHARACTER_FREQ:
            score = score + CHARACTER_FREQ[c]
    return score



def get_plain_text(hex_string):
    text_list = []
    for i in range(256):
        text = denc_xor(hex_string, chr(i))
        score = calc_score(text)
        result = {
            'key':chr(i),
            'plain_text':text,
            'score':score
        }
        text_list.append(result)
    return sorted(text_list, key = lambda i: i['score'])[-1]

def main():
    data = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    '''Output: Cooking MC's like a pound of bacon'''
    print(get_plain_text(data))

if __name__ == '__main__':
    main()