# 컨베이어 벨트 위의 로봇

import sys
from collections import deque, Counter

input = sys.stdin.readline
n,k = map(int,input().split())
a = deque(list(map(int,input().split())))
robot = deque([0] * n)
ans = 1

while True:
    a.rotate(1) # 벨트 한 번 이동
    robot.rotate(1) # 로봇 한 번 이동
    robot[-1] = 0 # 마지막 위치에 있는 로봇 내림

    # 벨트 내구도 1 이상 & 로봇이 없을 때
    if robot[0] == 0 and a[0] >= 1:
        robot[0] = 1
        a[0] -= 1

    # 벨트 내구도 1 이상 & 로봇 있을 때
    for i in range(n-1,-1,-1):
        if robot[i] == 1 and a[i + 1] >= 1:
            robot[i + 1] = 1
            robot[i] = 0
            a[i+1] -= 1

    robot[-1] = 0 # 마지막 위치에 있는 로봇 내림
    ans += 1

    if Counter(a)[0] >= k:
        break

print(ans)