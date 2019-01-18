'''Challenges   Set 2   Challenge 9    Implement PKCS#7 padding'''

def padding_pkcs7(string, block_size):
    l = block_size - len(string)
    for i in range(l):
        string = string + chr(l)
    return string

def main():
    data = "YELLOW SUBMARINE"
    print('%x', padding_pkcs7(data, 20))

if __name__ == '__main__':
    main()