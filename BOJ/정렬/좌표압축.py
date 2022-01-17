# 18870

n = int(input())
n_list = list(map(int,input().split()))

c_list = sorted(list(set(n_list)))
n_dict = {value:idx for idx,value in enumerate(c_list)}

for i in n_list:
    print(n_dict[i],end = ' ')


# 시간 초과
n = int(input())
n_list = list(map(int,input().split()))

c_list = sorted(list(set(n_list)))

for i in n_list:
    print(c_list.index(i),end = ' ')