# 분해합
# 브루트포스 알고리즘

n = int(input())

for i in range(1,n+1):
    gen = sum(map(int,str(i)))
    result = i + gen

    # result랑 n이랑 같으면 i 출력(가장 작은 값)
    if result == n:
        print(i)
        break

    # 생성자가 없을 경우 0 출력
    if i == n:
        print(0)