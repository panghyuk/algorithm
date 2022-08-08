# 페이지 세기

while True:
    n = int(input())
    ans = set()

    if n == 0:
        exit()

    else:
        pages = list(input().split(','))

        for page in pages:
            if '-' in page:
                low, high = list(page.split('-'))
                low, high = int(low), int(high)

                if low > high:
                    continue
                    
                else:
                    if high > n:
                        high = n
                        for i in range(low, high+1):
                            ans.add(i)
                    else:
                        for i in range(low, high+1):
                            ans.add(i)
            else:
                page = int(page)

                if page > n:
                    continue
                else:
                    ans.add(page)

        print(len(ans))