# N in [1,100,000]
# elem in [1, 1B]

def solution(H):
    stack = []
    index_max = max(range(len(H)), key=H.__getitem__)

    # sorted_H = H[:].sort()

    cuboid_count = 1
    local_max = H[0]
    i = 1
    while i < len(H):
        # stack.append(H[i] - min_H)
        if H[i] > H[i-1]:
            if H[i] != local_max:
                cuboid_count += 1
        elif H[i] < H[i-1]:
            cuboid_count += 1
            local_max = H[i]
        i += 1

    return cuboid_count


if __name__ == '__main__':
    print("Should be 7: " + str(solution([8,8,5,7,9,8,7,4,8])))
    # print("Should be 6: " + str(solution([7,5,2,7,2,7,4,7])))
    # print("Should be 3: " + str(solution([2,1,3])))
    print("Should be 1: " + str(solution([2])))

    # print("Laura: " + str(solution([2,1,3])))

    # import random
    # g1000 = [4]*17000 + random.choices(range(100000), k=83000)
    # print(solution(g1000))
