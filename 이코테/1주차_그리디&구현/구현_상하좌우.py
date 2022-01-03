# 책 풀이
n = int(input())
x,y = 1,1
plans = input().split()

# L,R,U,D 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L','R','U','D']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n: # 공간을 벗어나는 경우 무시
        continue # 코드를 실행하지 않고 건너 뜀
    x,y = nx, ny

print(x,y)