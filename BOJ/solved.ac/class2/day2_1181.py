# 정렬 알고리즘
# 단어 정렬

n = int(input())
w_list = []

for i in range(n):
    word = str(input())
    word_cnt = len(word) # 단어 길이
    w_list.append((word,word_cnt))

# 중복 삭제
w_list = list(set(w_list))

# 단어 정렬(글자 수, 알파벳)
result = sorted(w_list, key = lambda x : (x[1],x[0]))

for word,len in result:
    print(word)