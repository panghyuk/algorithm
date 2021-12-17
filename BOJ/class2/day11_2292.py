# 벌집
n=int(input())
f=1
plus=6
room=1
if n==1:
    print(1)
else:
    while True:
        f += plus
        room += 1
        if n <= f:
            print(room)
            break
        else:
            plus += 6