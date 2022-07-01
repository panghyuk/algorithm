# 1931

n = int(input())
meet = []

for _ in range(n):
    a,b = map(int,input().split())
    meet.append([a,b])

meet.sort(key = lambda x: (x[1],x[0]))
cnt = 0
end = 0

for i in meet:
    if end <= i[0]:
        end = i[1]
        cnt += 1     

print(cnt)