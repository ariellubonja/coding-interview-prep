def solution(A):
    if len(A) < 2:
        return 0
    max_slice = 0
    stock_start = 0
    i = 1
    while i < len(A):
        if A[i] - A[stock_start] > 0:
            max_ending = A[i] - A[stock_start]
        else:
            stock_start += 1
            # Will get post-incremented
            if i > stock_start:
                i = stock_start
            max_ending = 0
        max_slice = max(max_slice, max_ending)
        i += 1
    return max_slice

# def solution(A):
#     if len(A) < 2:
#         return 0
#     result = 0
#     for p in range(len(A)):
#         profit = 0
#         for q in range(p, len(A)):
#             profit = A[q] - A[p]
#             result = max(result, profit)
#     return result


if __name__ == '__main__':
    # print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
    print(solution([8, 9, 3, 6, 1, 2]))