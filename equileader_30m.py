# 33% solution. 0% performance

import math

def solution(A):
    B = A[:]
    B.sort()

    leader = B[math.floor(len(B)/2)]

    leader_indices = [i for i, x in enumerate(A) if x == leader]
    total_leader_count = len(leader_indices)

    left_leader_count = 0
    right_leader_count = total_leader_count
    equileader_count = 0
    for index in leader_indices:
        left_array = A[:index+1]
        right_array = A[index+1:]
        left_leader_count += 1
        right_leader_count -= 1
        if left_leader_count > len(left_array)/2 and right_leader_count > len(right_array)/2:
            equileader_count += 1

    return equileader_count


if __name__ == '__main__':
    print(solution([9,9,9,7,6]))
    print(solution([0,0,0]))
    print(solution([1,1,3,1]))
    print(solution([4]))
    print(solution([4, 3, 4, 4 ,4, 2]))
    # print([4][:1])