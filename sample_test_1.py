# 33% solution. 0% performance
# N in [1-100,000]
# each element in [-1M, 1M]
# A = [-1], return 1

def solution(A):
    positive_a = [num for num in A if num > 0]

    if len(positive_a) == 0:
        return 1

    # positive_a.sort()

    if min(positive_a) != 1:
        return 1

    max_A = max(positive_a)
    # Do range of (max_A)

    subscription = (set(range(1, max_A + 1)) - set(positive_a))

    if len(subscription) == 1:
        missing = subscription.pop()
    else:
        missing = max_A + 1

    return missing


if __name__ == '__main__':
    print(solution([1,3,6,4,1,2]))
    print(solution([0,0,0]))
    print(solution([1,1,3,1]))
    print(solution([4]))
    print(solution([4, 3, 4, 4 ,4, 2]))
    print(solution([-1]))
    # print([4][:1])