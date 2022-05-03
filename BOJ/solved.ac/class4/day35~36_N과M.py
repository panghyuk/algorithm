# # 15649 백트래킹
# n,m = map(int,input().split())
# ans = []

# def dfs():
#     if len(ans) == m:
#         print(" ".join(map(str,ans)))
#         return
        
#     for i in range(1,n+1):
#         if i in ans:
#             continue
#         ans.append(i)
#         dfs()
#         ans.pop()

# dfs()

# # 15650 백트래킹(dfs)
# n,m = map(int,input().split())
# ans = []

# def dfs(s):
#     if len(ans) == m:
#         print(" ".join(map(str,ans)))
#         return

#     for i in range(s,n+1):
#         if i not in ans:
#             ans.append(i)
#             dfs(i+1)
#             ans.pop()

# dfs(1)

# # 15651 백트래킹
# n,m = map(int,input().split())
# ans = []

# def dfs():
#     if len(ans) == m:
#         print(" ".join(map(str,ans)))
#         return
        
#     for i in range(1,n+1):
#         ans.append(i)
#         dfs()
#         ans.pop()

# dfs()

# # 15652 백트래킹
# n,m = map(int,input().split())
# ans = []

# def dfs():
#     if len(ans) == m:
#         print(" ".join(map(str,ans)))
#         return
        
#     for i in range(1,n+1):
#         if len(ans) == 0:
#                 ans.append(i)
#                 dfs()
#                 ans.pop()
#         else:
#             if ans[-1] <= i:
#                 ans.append(i)
#                 dfs()
#                 ans.pop()

# dfs()

# # 15654 백트래킹
# n,m = map(int,input().split())
# n_list = list(map(int,input().split()))
# n_list.sort()
# visit = [False] * n # 방문처리
# ans = []

# def dfs():
#     if len(ans) == m:
#         print(" ".join(map(str,ans)))
#         return
#     for i in range(n):
#         if not visit[i]:
#             visit[i] = True
#             ans.append(n_list[i])
#             dfs()
#             ans.pop()
#             visit[i] = False # 방문 False로 다시 돌려놓기
# dfs()

# 15656