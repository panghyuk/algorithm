# 달팽이는 올라가고 싶다

import math

a,b,v = map(int,input().split())
day = math.ceil((v-b)/(a-b)) # 목표 높이: v - b
print(day)

