# 영화감독 숌
# 브루트포스, 완전탐색

# sol.1
n = int(input())
war = 666

while True:
    if '666' in str(war):
        n -= 1
        if n == 0:
            print(war)
            break
    war += 1

# sol.2
n = int(input())
war = 666
cnt = 0

while True:
    if '666' in str(war):
        cnt += 1
    if cnt == n:
        print(war)
        break
    war += 1