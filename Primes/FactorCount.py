def solution(N):
    if N == 1:
        return 1
    num_factors = 2

    # if N % 2 == 0:
    #     num_factors += 2

    import math
    half = math.floor(N/2)

    max_val = half + 1
    i = 2
    while i < max_val:
        if N % i == 0:
            if i == (N / i):
                num_factors += 1
            else:
                num_factors += 2
            max_val = (N / i) - 1
        i += 1

    return num_factors


# They've made the observation that half the factors are <= sqrt(N)
def codility_solution(N):
    i = 1
    num_factors = 0
    while i * i < N:
        if N % i == 0:
            num_factors += 2
        i += 1
    if i * i == N:
        num_factors += 1
    return num_factors


if __name__ == '__main__':
    print(solution(24))
    print(solution(4))
    print(codility_solution(4))
