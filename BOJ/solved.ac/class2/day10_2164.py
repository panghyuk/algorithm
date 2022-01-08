# 카드 2
# 자료 구조, 큐
from collections import deque

n = int(input())
n_list = deque([i for i in range(1,n+1)])

while (len(n_list)>1):
    n_list.popleft()
    n_list.append(n_list.popleft())

print(n_list[0])


# # 내 풀이(시간 초과)
# n = int(input())
# n_list = [i for i in range(1,n+1)]

# while True:
#     if len(n_list)==1:
#         print(n_list[0])
#         break
#     else:
#         n_list.pop(0)
#         n_list.append(n_list.pop(0))