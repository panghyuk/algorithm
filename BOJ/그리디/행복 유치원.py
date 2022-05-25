# 13164

n,k = map(int,input().split())
student = list(map(int,input().split()))
cost = []

for i in range(n-1): # 인접한 학생의 키 차이
    cost.append(student[i+1] - student[i])

cost.sort()

print(sum(cost[:n-k])) # (n-k) 만큼 키 차이 무시