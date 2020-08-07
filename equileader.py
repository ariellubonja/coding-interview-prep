import math
import random


def solution(A):
    overall_leader = find_leader(A)

    return find_equileader_count(A, overall_leader)


def find_leader(numbers):
    # Sort so we can find leader in O(NlogN). Python sorts in place, so we need to copy by value
    B = numbers[:]
    B.sort()
    return B[math.floor(len(numbers)/2)]


def find_equileader_count(A, overall_leader):
    equileader_count = 0

    # Go to first leader instance to save time on other numbers
    first_index = A.index(overall_leader)
    first_half_leader_count = 0
    second_half_leader_count = A.count(overall_leader)

    for a in range(first_index, len(A)):
        if A[a] == overall_leader:
            first_half_leader_count += 1
            second_half_leader_count -= 1
        # A[0:a] doesn't include A[a]
        if first_half_leader_count > len(A[0:a + 1])/2 and second_half_leader_count > len(A[a + 1:len(A)])/2:
            # print(A[a + 1:len(A)])
            equileader_count += 1

    return equileader_count


# def is_leader(A, number):
#     return A.count(number) > len(A) / 2


if __name__ == '__main__':
    # print(solution([4, 3, 4, 4, 4, 2]))
    # print(solution([1]))
    # print(solution([4, 4, 2, 5, 3, 4, 4, 4]))
    #
    # g10000 = [4]*5001 + random.sample(range(100000), 4999)
    # random.shuffle(g10000)
    # print(solution(g10000))

    g50000 = [4]*25001 + random.sample(range(100000), 24999)
    random.shuffle(g50000)
    print(solution(g50000))

    # g100000 = [4]*50001 + random.sample(range(100000), 49999)
    # random.shuffle(g100000)
    # print(solution(g100000))
