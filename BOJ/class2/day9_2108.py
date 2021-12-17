# 통계학
# 구현, 정렬
import sys
from collections import Counter

n = int(sys.stdin.readline())
n_list = []

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

# 산술평균
print(round(sum(n_list)/n))

# 중앙값
print(n_list[n//2])

# 최빈값
cnt = Counter(n_list).most_common()

if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

# 범위
print(n_list[-1] - n_list[0])
