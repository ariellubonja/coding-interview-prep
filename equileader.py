def solution(A):
    leader_indexes = []
    numbers_processed = []
    overall_leader = None
    i = 0
    while i < len(A):
        if A[i] not in numbers_processed:
            if is_leader(A, A[i]):
                leader_indexes = [i for i, x in enumerate(A) if x == A[i]]
                overall_leader = A[i]
                break
            numbers_processed.append(A[i])
        i += 1

    equileader_count = 0

    for a in leader_indexes:
        # A[0:a] doesn't include A[a]
        if a < len(A) and is_leader(A[0:a + 1], overall_leader) and is_leader(A[a + 1:len(A)], overall_leader):
            # print(A[a + 1:len(A)])
            equileader_count += 1

    return equileader_count


def is_leader(A, number):
    return A.count(number) > len(A) / 2


if __name__ == '__main__':
    print(solution([4, 3, 4, 4, 4, 2]))
    print(solution([1]))
