# Task 3: Focus on efficiency
# A = [N*int, int(S)]
# Count number of CONTINUOUS fragments of A that has mean equal to S
# If S > 1B, return 1B

# E.g.
# A = [2,1,3] S=2 should return 3, because mean(2), mean(1,3) and mean(2,1,3) are all =2=S
# A = [0,4,3,-1] S=2 should return 2, because mean(0,4) and mean(4,3,-1) are all =2=S
# A = [2,1,4] S=3 should return 0, because no sublist can have mean of 3

# len(A) < 100,000
# S in [-1B, 1B]
# A-elem in [-1B, 1B]


# So we need combination of all elems, whether they mean() = S
# Not combinatorics, they are continuous subsets


def solution(A, S):
    import itertools

    # A = [2,1,3]
    # S = 2
    # tot_sum = [sum([1 for i, x in enumerate(A) if (x / (i+1)) == S] for gimi in [list(itertools.accumulate(A[i:])) for i in range(len(A))]]
    tot_sum = [sum([1 for i, x in enumerate(gimi) if (x / (i+1)) == S]) for gimi in [list(itertools.accumulate(A[i:])) for i in range(len(A))]]
    return tot_sum

    # return sum([sum([1 for i, x in enumerate(gimi) if (x / (i+1)) == S]) for gimi in [list(itertools.accumulate(A[i:])) for i in range(len(A))]])


# def solution(A, S):
#     sum = 0
#     if sum > 1000000000:
#         return 1000000000
#     return sum


if __name__ == '__main__':
    import random
    # print(solution([2,1,3], 2))
    # print(solution([0,4,3,-1], 2))
    # print(solution([2,1,4], 3))
    # print(solution([2], 2))
    #
    # print("Laura: " + str(solution([2, 3, 9, 8, 7, 9, 1, 4, 9, 9, 8, 2, 8, 8, 1, 4, 4, 6, 7, 8, 8, 8, 0, 7, 8, 8, 6, 9, 6, 9, 0, 6, 8, 9, 4, 1, 1, 0, 6, 1, 1, 9, 4, 5, 9, 8, 9, 9, 1, 2, 4, 0, 9, 5, 7, 3, 6, 6, 7, 3, 5, 9, 7, 6, 4, 5, 0, 0, 2, 5, 1, 1, 7, 5, 4, 5, 8, 5, 8, 6, 1, 2, 1, 7, 4, 2, 9, 9, 4, 4, 8, 1, 4, 8, 8, 3, 8, 7, 7, 2], 5)))

    g1000 = random.choices(range(1000000), k=100000)
    s = round(sum(g1000)/100000)
    print(solution(g1000, 100))
