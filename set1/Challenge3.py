'''Challenges   Set 1   Challenge 3    Single-byte XOR cipher'''
data = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
def de_enc_xor(crypto, key):
    hex_data = crypto.decode('hex')
    buf = []
    for ch in hex_data:
        buf.append(chr(ord(ch) ^ ord(key)))
    return ''.join(buf)

for i in range(128):
    text = de_enc_xor(data, chr(i))
    if text == 'Cooking MC\'s like a pound of bacon':
        print('Done')
        break
'''Output: Cooking MC's like a pound of bacon'''