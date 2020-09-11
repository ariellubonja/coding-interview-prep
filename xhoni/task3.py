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

    return sum([sum([1 for i, x in enumerate(gimi) if (x / (i+1)) == S]) for gimi in [list(itertools.accumulate(A[i:])) for i in range(len(A))]])


if __name__ == '__main__':
    import random
    print(solution([2,1,3], 2))
    print(solution([0,4,3,-1], 2))
    print(solution([2,1,4], 3))
    print(solution([2], 2))

    g1000 = random.sample(range(1000000), 10000)
    print(solution(g1000, 100))
