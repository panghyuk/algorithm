# 단어 공부
# 구현, 문자열

word = input().upper()
word_list=list(set(word))
cnt_list=[]

for i in word_list:
    cnt = word.count(i)
    cnt_list.append(cnt)

# cnt_list에 
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    idx = cnt_list.index(max(cnt_list))
    print(word_list[idx])
