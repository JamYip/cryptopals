'''
hex_string is a hex string without 0x, such as 010249ff
return a base64 string
'''
def hex2base64(hex_string):
    hex_data = hex_string.decode('hex')
    b64_encode = hex_string.b64encode(hex_data)
    return b64_encode

def main():
    data = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64 = hex2base64(data)
    '''output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'''
    print(b64)

if __name__ == '__main__':
    main()