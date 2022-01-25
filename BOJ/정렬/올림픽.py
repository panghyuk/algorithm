# 8979

''' 리스트 활용 (100점) '''
n,k = map(int,input().split())
ranking = [[] for _ in range(n+1)]

for _ in range(n):
    country, gold, silver, bronze = map(int,input().split())
    ranking[country] = [gold,silver,bronze]

cnt = 1

for i in range(1,n+1):
    if ranking[k][0] < ranking[i][0]:
        cnt += 1
    elif ranking[k][0] == ranking[i][0]:
        if ranking[k][1] < ranking[i][1]:
            cnt += 1
        elif ranking[k][1] == ranking[i][1]:
            if ranking[k][2] < ranking[i][2]:
                cnt += 1

print(cnt)


''' 희찬's 풀이 '''

n,k = map(int,input().split())
nations = [list(map(int,input().split())) for _ in range(n)]

#1.금메달(1) 2.은메달(2) 3.동메달(3)
nations.sort(key=lambda x:(-x[1],-x[2],-x[3]))
cnt = 0

for i in range(n):
  cnt += 1
  if nations[i][0] == k:
    if i == 0:
      print(cnt)
      break

    if nations[i-1][1:] == nations[i][1:]: # 동점 처리
      cnt -= 1
      print(cnt)
      break

    print(cnt)
    break