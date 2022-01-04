# Divisors of a number gamified

def towerBreakers(n, m):
    if m == 1:
        return 2

    if n % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    print(towerBreakers(1, 4))
