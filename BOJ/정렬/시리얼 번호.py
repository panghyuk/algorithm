# 1431

n = int(input())
serial = []

for _ in range(n):
    serial.append(input())

def total_sum(arr):
    ans = 0
    for i in arr:
        if i.isdigit():
            ans += int(i)
    return ans

serial.sort(key = lambda x: (len(x),total_sum(x),x))

for i in serial:
    print(i)