# 2437

n = int(input())
pendulum = list(map(int,input().split()))
pendulum.sort()
w = 1

for i in pendulum:
    if w < i:
        break
    w += i

print(w)