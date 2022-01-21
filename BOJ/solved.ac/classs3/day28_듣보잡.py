# 1764
# 집합 활용

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
hear = set()
see = set()

for _ in range(n):
    hear.add(input().rstrip())

for _ in range(m):
    see.add(input().rstrip())

result = sorted(list(hear & see))

print(len(result))
for i in result:
    print(i)
