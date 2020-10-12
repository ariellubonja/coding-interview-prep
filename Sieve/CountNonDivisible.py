def solution(A):
    curr_count_non_divisible = 0
    count_non_divisible_array = [0] * len(A)
    for i in range(len(A)):
        for other_elem in A:
            if A[i] % other_elem != 0:
                curr_count_non_divisible += 1
        count_non_divisible_array[i] = curr_count_non_divisible
        curr_count_non_divisible = 0
    return count_non_divisible_array


if __name__ == '__main__':
    print(solution([3,1,2,3,6]))
