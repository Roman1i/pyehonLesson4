from random_polynomial import polynomial

def factors(lst):
    facs = []
    for i in range(len(lst) - 2):
        if lst[i] not in ["+", "-"] and lst[i + 1] != "=":
            if i > 1 and lst[i - 1] == "-":
                facs.append("-" + lst[i][:lst[i].find('x')])
            else:
                facs.append(lst[i][:lst[i].find('x')])
        elif lst[i + 1] == "=":
            if i > 1 and lst[i - 1] == "-":
                facs.append("-" + lst[i])
            else:
                facs.append(lst[i])

    return facs


polynomial('5.1', 2)
polynomial('5.2', 2)

with open('5.1', 'r') as f:
    lst1 = f.readline().split()
    print(lst1)
    f1 = factors(lst1)
    print(f1)

with open('5.2', 'r') as f:
    lst2 = f.readline().split()
    print(lst2)
    f2 = factors(lst2)
    print(f2)

a = int(f1[0]) + int(f2[0])
b = int(f1[1]) + int(f2[1])
c = int(f1[2]) + int(f2[2])

with open('task5', 'w') as result:
    result.write(f'{a}x^2 ')
    if b > 0:
        result.write(f'+ {b}x ')
    else:
        result.write(f'- {abs(b)}x ')
    if c > 0:
        result.write(f'+ {c} ')
    else:
        result.write(f'- {abs(c)} ')
    result.write('= 0')
