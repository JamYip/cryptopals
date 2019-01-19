'''Challenges   Set 1   Challenge 8    Detect AES in ECB mode'''
'''ECB分组，如果明文的片段相同，则对应的密文片段相同'''
with open('./8.txt', 'r') as f:
    line = f.readline().replace('\r','').replace('\n','')
    
    while line:
        i = 0
        for i in range(len(line) // 32):
            sub = line[i * 32 : (i + 1) * 32]
            if line.find(sub, (i + 1) * 32) >= 0:
                print(line)
                break
        line = f.readline().replace('\r','').replace('\n','')