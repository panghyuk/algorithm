# 프린터 큐

test = int(input())

for i in range(test):
    n,m = map(int,input().split())
    w_list = list(map(int,input().split()))
    idx = [0 for _ in range(n)]
    idx[m] = 1

    cnt = 0

    while True:
        if w_list[0] == max(w_list):
            cnt += 1

            if idx[0] == 1:
                print(cnt)
                break
            else:
                w_list.pop(0)
                idx.pop(0)
        else:
            w_list.append(w_list.pop(0))
            idx.append(idx.pop(0))