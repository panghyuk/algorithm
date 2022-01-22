from bisect import bisect_left,bisect_right

# 값이 [left_value,right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(arr,left_value,right_value):
    right_idx = bisect_right(arr,right_value)
    left_idx = bisect_left(arr,left_value)
    return right_idx - left_idx

n,x = map(int,input().split())
arr = list(map(int,input().split()))

# 값이 [x,x] 범위에 있는 데이터의 개수 계산
cnt = count_by_range(arr,x,x)

# 값이 x인 원소가 존재하지 않는다면
if cnt == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(cnt)