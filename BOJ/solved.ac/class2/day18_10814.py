# 나이순 정렬
# 정렬

n = int(input())
s_list = []

for i in range(n):
    age,name = input().split()
    age = int(age)
    s_list.append([age,name])
    
s_list.sort(key = lambda x:x[0])

for i in s_list:
    print(i[0],i[1])