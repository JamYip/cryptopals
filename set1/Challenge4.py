'''Challenges   Set 1   Challenge 4    Detect single-character XOR'''
import Challenge3

file_name = '4.txt'
with open(file_name) as f:
    data = f.readline().replace('\r','').replace('\n','')
    data.decode('hex')
    text_list = []
    while data:
        det = Challenge3.get_plain_text(data)
        text_list.append(det)
        data = f.readline().replace('\r','').replace('\n','')
    print(sorted(text_list, key = lambda i: i['score'])[-1:])
