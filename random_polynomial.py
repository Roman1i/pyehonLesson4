import random


def polynomial(file_name, k):
    with open(file_name, 'w') as f:
        for i in range(k):
            num = random.randint(1, 99)
            p = random.randint(0, 1)
            if k - i == 1:
                if p == 0:
                    f.write(f' - {num}x')
                if p == 1:
                    f.write(f' + {num}x')
            else:
                if k - i == k:
                    f.write(f'{num}x^{k - i}')
                elif p == 0:
                    f.write(f' - {num}x^{k - i}')
                elif p == 1:
                    f.write(f' + {num}x^{k - i}')

        x = random.randint(0, 1)
        if x == 0:
            f.write(' - ' + str(random.randint(1, 99)) + ' = 0')
        if x == 1:
            f.write(' + ' + str(random.randint(1, 99)) + ' = 0')
