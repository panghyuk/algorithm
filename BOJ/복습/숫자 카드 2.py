# 10816
''' 이분 탐색 활용 '''
n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
given = list(map(int,input().split()))



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