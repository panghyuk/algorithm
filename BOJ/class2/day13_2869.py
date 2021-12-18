# 달팽이는 올라가고 싶다

import math

a,b,v = map(int,input().split())

# 날짜 계산: (a - b) * n + a = v
day = math.ceil((v-a)/(a-b))+1 # math.ceil: 올림
print(day)

