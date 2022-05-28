# 10816
''' 이분 탐색 활용 '''
n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
given = list(map(int,input().split()))

cnt = {}

for x in card:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

s,e = 0,len(card)

def bin(arr,tar,s,e):
    if s > e:
        return 0
    mid = (s+e) // 2

    if arr[mid] == tar:
        return cnt[tar]
    elif arr[mid] > tar:
        return bin(arr, tar, s, mid - 1)
    else:
        return bin(arr, tar, mid + 1, e)

for i in given:
    print(bin(card, i, 0, len(card)-1), end = " ")
    


''' 딕셔너리 활용 '''
# import sys
# input = sys.stdin.readline

# n = int(input())
# card = list(map(int,input().split()))
# max_num = max(card)
# min_num = min(card)
# res = {}

# for i in range(n):
#     if card[i] in res.keys():
#         res[card[i]] += 1
#     else:
#         res[card[i]] = 1

# m = int(input())
# given = list(map(int,input().split()))

# for j in given:
#     if j not in res.keys():
#         print(0, end = ' ')
#     else:
#         print(res[j],end = ' ')