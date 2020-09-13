# Task 2: Focus on efficiency
# Summer - N days free
# Location "names" go from 0 to N-1

# Smallest nr of days to visit all


# Start with slow but correct solution

# N in [1, 100k]
# Each in n in [0, N-1]

# Return min nr of vacation days to visit all
def solution(A):
    distinct = set(A)

    min_vac_time = len(A)

    # From 3 to N, this determines the size of the sliding window
    for vacation_time in range(len(distinct), len(A)-1):
        for starting_day in range(len(A) - len(distinct)):
            if distinct == set(A[starting_day:starting_day+vacation_time]):
                return vacation_time

    return min_vac_time


if __name__ == '__main__':
    import random
    print(solution([2,1,1,3,2,1,1,3]))
    print(solution([7,5,2,7,2,7,4,7]))
    print(solution([2,1,3]))
    print(solution([2]))

    # g1000 = random.sample(range(1000000), 10000)
    # print(solution(g1000, 100))
