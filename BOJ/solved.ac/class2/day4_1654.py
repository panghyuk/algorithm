# 랜선 자르기
# 이분 탐색/ 매개 변수 탐색
# import sys 활용?

k,n = map(int,input().split())
lan_list = []

for _ in range(k):
    lan_list.append(int(input()))

start, end = 1 , max(lan_list)

# 이진 탐색
while start <= end:
    # 중간 지정
    mid = (start+end)//2
    # 랜선 개수
    cnt = 0

    for i in lan_list:
        cnt += i // mid
    
    if cnt >= n: # 분할된 개수가 n보다 크면 start 값 증가
        start = mid + 1
    else: # 분할된 개수가 n보다 작으면 end 값 감소
        end = mid - 1

print(end)

