# 1541

data = input().split('-')
result = 0

for i in data[0].split('+'):
    result += int(i)

for j in data[1:]:
    for k in j.split('+'):
        result -= int(k)

print(result)