# 1003
# DP

zero = [1,0,1]
one = [0,1,1]
n = int(input())

def fibo_cnt(num):
    length = len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print("{} {}".format(zero[num],one[num]))

for i in range(n):
    fibo_cnt(int(input()))