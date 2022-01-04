def fibo_count(num):
    if num > 2:
        for i in range(3,num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print("{} {}".format(zero[num],one[num]))

zero = [1,0,1]
one = [0,1,1]
n = int(input())

for i in range(n):
    fibo_count(int(input()))