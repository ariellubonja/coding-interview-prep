# def solution(A):
#     if len(A) < 2:
#         return 0
#     max_ending = max_slice = 0
#     current_slice_start = max_slice_start = 0
#     current_slice_end = max_slice_end = 1
#     stock_start = A[0]
#     i = 1
#     while i < len(A):
#         max_ending = max(0, max_ending + A[i] - A[stock_start])
#         if max_ending > max_slice:
#             max_slice = max_ending
#             max_slice_end = i
#         max_slice = max(max_slice, max_ending)
#         i += 1
#     return max_slice

def solution(A):
    if len(A) < 2:
        return 0
    result = 0
    for p in range(len(A)):
        profit = 0
        for q in range(p, len(A)):
            profit = A[q] - A[p]
            result = max(result, profit)
    return result