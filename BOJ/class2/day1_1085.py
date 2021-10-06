# 직사각형에서 탈출
# 수학 / 기하학

x,y,w,h = map(int,input().split())
print(min([x,y,w-x,h-y]))

# 나의 풀이
if (w-x) > x and (h-y) > y:
    if x > y:
        print(y)
    else:
        print(x)

elif (w-x) > x and (h-y) < y:
    if x > (h-y):
        print(h-y)
    else:
        print(x)

elif (w-x) < x and (h-y) > y:
    if (w-x) > y:
        print(y)
    else:
        print(w-x)

else:
    if (w-x) > (h-y):
        print(h-y)
    else:
        print(w-x)

