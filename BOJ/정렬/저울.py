# 2437

n = int(input())
pendulum = list(map(int,input().split()))
pendulum.sort()
w = 1

for i in pendulum:
    if w < i: # 더한 추의 무게보다 새로운 추의 무게가 더 무거울 때 종료
        break
    w += i

print(w)