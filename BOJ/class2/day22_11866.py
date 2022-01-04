# 요세푸스 문제 0
# 자료구조(큐)

# deque 활용
from collections import deque

n,k = map(int,input().split())
q = deque()
result = []

for i in range(n):
    q.append(i+1)

while q:
    for j in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print('<',end = '')
for i in range(n-1):
    print("%d, "%result[i], end = '')
print(result[-1],end = '')
print('>')

# 내 풀이
n,k = map(int,input().split())
que = [i for i in range(1,n+1)]
idx = 0
result = []

while que:
    idx += (k-1)
    if idx > len(que)-1:
        idx %= len(que)
    result.append(que.pop(idx))

print('<',end = '')
for i in range(n-1):
    print(str(result[i]) + ', ',end = '')
print(result[-1],end = '')
print('>')
