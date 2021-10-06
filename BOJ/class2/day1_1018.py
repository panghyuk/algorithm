# 체스판 다시 칠하기
# 브루트포스(Brute Force), 완전탐색

n,m = map(int,input().split())

board = list()
cnt = list()

for _ in range(n):
    board.append(input())

for a in range(n-7):
    for b in range(m-7):
        idx_w = 0 # 시작이 W, 바뀐 갯수
        idx_b = 0 # 시작이 B, 바뀐 갯수

        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0: # 시작점과 같은 색
                    if board[i][j] != 'W':
                        idx_w += 1
                    else:
                        idx_b += 1
                else: # 시작점과 다른 색
                    if board[i][j] != 'B':
                        idx_w += 1
                    else:
                        idx_b += 1
        cnt.append(min(idx_w,idx_b))

print(min(cnt))

# # 지섭풀이
# import copy
# n,m = map(int,input().split())
# # n줄의 흑백 칸 생성
# chess = []
# chess88=[]
# for _ in range(n):
#     col = list(input())
#     chess.append(col)
# for i in range(n-8+1): # ex) n= 9 이면 range(2): 세로는 0,1일때 두가지 경우가 있음 ->총 4개의 8*8체스판이 생김
#     chess_sero= chess[i:i+8]  # i= 0 일 때, chess_sero = chess[0:8], i=1 일 때,chess_sero = chess[1:9] 
#     for j in range(m-8+1): # 세로줄이 정해졌으니 , 가로줄 정의 
#         chess_garosero =[] # 8*8 사각형
#         for k in chess_sero:
#             chess_garosero.append(k[j:j+8]) 
#         chess88.append(chess_garosero)
# B_first=['B','W','B','W','B','W','B','W']
# W_first = B_first[::-1]
# sol = [B_first,W_first]*4
# reverse_sol = sol[::-1]

# sol_list=[]
# for row in chess88:
#     cnt1=0 #첫 번째 칸을 B로 색칠한다면..? 
#     chess_copy=copy.deepcopy(row)
#     for i in range(8):
#         for j in range(8):
#             if chess_copy[0][0]=='B':
#                 pass
#             else:
#                 chess_copy[0][0]='B'
#                 cnt1+=1
#             if sol[i][j]!=chess_copy[i][j]:
#                 chess_copy[i][j]=sol[i][j]
#                 cnt1+=1
#             else:
#                 pass
#     cnt2=0 #첫 번째 칸을 W로 색칠한다면..? 
#     chess_copy=copy.deepcopy(row)
#     for i in range(8):
#         for j in range(8):
#             if chess_copy[0][0]=='W':
#                 pass
#             else:
#                 chess_copy[0][0]='W'
#                 cnt2+=1
#             if reverse_sol[i][j]!=chess_copy[i][j]:
#                 chess_copy[i][j]=reverse_sol[i][j]
#                 cnt2+=1
#             else:
#                 pass           
#     sol_list.append(min(cnt1,cnt2))
# print(min(sol_list))