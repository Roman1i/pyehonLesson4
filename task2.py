n = int(input())
count = 2
res =[]

for i in range(n):
    if n % count != 0:
        count += 1
    else:
        res.append(count)
        n = n / count
        count = 2

print(res)

