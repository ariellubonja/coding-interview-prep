# Task 2: Focus on efficiency
# Summer - N days free
# Location "names" go from 0 to N-1

# Smallest nr of days to visit all


# Start with slow but correct solution

# N in [1, 100k]
# Each in n in [0, N-1]

# Return min nr of vacation days to visit all
# def solution(A):
#     distinct = set(A)
#
#     min_vac_time = len(A)
#
#     # import itertools
#
#     # The number of vacation days needs to be at least same as nr. of distinct locations
#     for vacation_time in range(len(distinct), len(A)-1):
#         gimi = set(True if distinct == set(A[starting_day:starting_day+vacation_time]) else False for starting_day in range(len(A) - len(distinct)))
#         if True in gimi:
#             return vacation_time
#         # if list(itertools.filterfalse(
#         #         lambda starting_day: distinct != set(A[starting_day:starting_day + vacation_time]),
#         #         range(len(A) - len(distinct)))):
#         #     return vacation_time
#         # for starting_day in range(len(A) - len(distinct)):
#         #     if distinct == set(A[starting_day:starting_day+vacation_time]):
#         #         return vacation_time
#
#     return min_vac_time


# Laura, slow
def solution(A):
    N = len(A)
    no_distinct = len(set(A))
    i = 0
    j= no_distinct -1
    current_hits = set(A[i:(j+1)])
    optimal = N
    while j < N:
        if len(current_hits) < no_distinct:
            j += 1
            if (j < N) and not(A[j] in current_hits):
                current_hits.add(A[j])
        else:
            if A[j] == A[i]:
                i += 1
            if((j-i+1) <= optimal):
                optimal = j-i+1
                # print("optimal", optimal)
            # this one's bad. I need to replace current_hits by a map. how many times each location has been visited
            if not(A[i] in A[(i+1):(j+1)]):
                current_hits.remove(A[i])
            i += 1
        # print(i, j, current_hits)
    return optimal

# optimum = shortest(A)


if __name__ == '__main__':
    import random

    print("Should be 3: " + str(solution([2,1,1,3,2,1,1,3])))
    print("Should be 6: " + str(solution([7,5,2,7,2,7,4,7])))
    print("Should be 3: " + str(solution([2,1,3])))
    # print("Should be 1: " + str(solution([2])))

    print("Laura: " + str(solution([2,1,3])))

    # g1000 = [4]*17000 + random.choices(range(100000), k=83000)
    # print(solution(g1000))
