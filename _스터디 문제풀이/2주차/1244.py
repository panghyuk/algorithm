# 스위치 켜고 끄기

n = int(input())
array = [0] + list(map(int,input().split()))
st = int(input())

def switch(a,b,arr):
    if a == 1: # 남자일 때
        for i in range(b,n+1,b):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1

    else: # 여자일 때
        if arr[b] == 0:
            arr[b] = 1
        else:
            arr[b] = 0

        for i in range(1,n//2):
            if b + i > n or b - i < 1:
                break
            if arr[b+i] == arr[b-i]:
                if arr[b+i] == 1:
                    arr[b-i] = 0
                    arr[b+i] = 0
                else:
                    arr[b-i] = 1
                    arr[b+i] = 1
            else:
                break
        return arr

for _ in range(st):
    sex, num = map(int,input().split())
    switch(sex,num,array)

for j in range(1,n+1):
    print(array[j],end = ' ')
    if j % 20 == 0:
        print()