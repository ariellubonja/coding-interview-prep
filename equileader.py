import math
import random


def solution(A):
    overall_leader = find_leader(A)

    equileader_count = 0

    for a in range(len(A)):
        # A[0:a] doesn't include A[a]
        if is_leader(A[0:a + 1], overall_leader) and is_leader(A[a + 1:len(A)], overall_leader):
            # print(A[a + 1:len(A)])
            equileader_count += 1

    return equileader_count


def find_leader(numbers):
    # Sort so we can find leader in O(NlogN). Python sorts in place, so we need to copy by value
    B = numbers[:]
    B.sort()
    return B[math.floor(len(numbers)/2)]


def is_leader(A, number):
    return A.count(number) > len(A) / 2


if __name__ == '__main__':
    # print(solution([4, 3, 4, 4, 4, 2]))
    # print(solution([1]))
    # print(solution([4, 4, 2, 5, 3, 4, 4, 4]))

    g10000 = [4]*5001 + random.sample(range(100000), 4999)
    random.shuffle(g10000)
    print(solution(g10000))
