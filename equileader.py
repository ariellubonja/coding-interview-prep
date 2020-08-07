import math


def solution(A):
    overall_leader = find_leader(A)
    # Find leader's indexes in the original array
    leader_indexes = [i for i, x in enumerate(A) if x == overall_leader]

    equileader_count = 0

    for a in leader_indexes:
        # A[0:a] doesn't include A[a]
        if a < len(A) and is_leader(A[0:a + 1], overall_leader) and is_leader(A[a + 1:len(A)], overall_leader):
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
    print(solution([4, 3, 4, 4, 4, 2]))
    print(solution([1]))
    print(solution([4, 4, 2, 5, 3, 4, 4, 4]))
