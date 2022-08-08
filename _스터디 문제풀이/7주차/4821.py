# 페이지 세기

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    ans = set()

    if n == 0:
        exit()

    else:
        pages = list(input().split(','))

        for page in pages:
            if '-' in page: # '-'을 포함할 때
                low, high = list(page.split('-'))
                low, high = int(low), int(high)

                if low > high: # low가 high보다 클 때
                    continue
                    
                else:
                    if high > n: # high가 n보다 클 때
                        high = n # high를 n으로 바꿈
                        for i in range(low, high+1):
                            ans.add(i)
                    else:
                        for i in range(low, high+1):
                            ans.add(i)

            else: # '-'을 포함하지 않을 때
                page = int(page)

                if page > n: # page(숫자)가 n보다 클 때
                    continue
                else:
                    ans.add(page)

        print(len(ans))