# 평균

n = int(input())
score_list = list(map(int,input().split()))

max_score = max(score_list)

for i in range(len(score_list)):
    score_list[i] = score_list[i]/max_score * 100

avg = sum(score_list)/n

print(avg)