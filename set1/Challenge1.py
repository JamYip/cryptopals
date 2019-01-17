'''Challenges   Set 1   Challenge 1  Convert hex to base64'''

import base64

data = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
hex_data = data.decode('hex')
b64_encode = base64.b64encode(hex_data)
'''output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'''
print(b64_encode)