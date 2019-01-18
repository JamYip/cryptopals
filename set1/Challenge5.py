'''Challenges   Set 1   Challenge 5    Implement repeating-key XOR'''
import struct



def enc_repeat_xor(plain_text, key):
   p = len(plain_text) // len(key)
   q = len(plain_text) % len(key)
   gen_key = ''
   for i in range(p):
      gen_key = gen_key + key
   gen_key = gen_key + key[0:q]

   arr = []
   for i,j in zip(plain_text, gen_key):
      arr.append(ord(i) ^ ord(j))
   return ''.join(struct.pack('<b', i) for i in arr).encode('hex')

def main():
   text = '''Burning 'em, if you ain't quick and nimble
   I go crazy when I hear a cymbal'''
   key = 'ICE'
   '''Output is 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''
   print(enc_repeat_xor(text, key))

if __name__ == '__main__':
   main()