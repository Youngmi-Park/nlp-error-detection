# input으로 문장이 들어오면 공백 단위로 자르고
# 각각의 단어를[MASK]로 바꿔서 문장을 만든다.

text = "i love you"
text_split = list(map(str,text.split()))
text_list = []

for i in range(len(text_split)):
    temp = list(text_split)
    temp[i] = '[MASK]'
    print(' '.join(map(str,temp)))
    text_list.append(' '.join(map(str,temp)))

print(text_list)
