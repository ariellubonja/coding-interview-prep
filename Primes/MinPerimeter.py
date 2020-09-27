# Minimal perimeter of rect whose area is N

def solution(N):
    import math
    starting_point = math.sqrt(N)

    if isinstance(starting_point, int):
        return 4*starting_point
    else:
        starting_point = math.floor(starting_point)

        while starting_point > 1:
            if N % starting_point == 0:
                return int(2*(starting_point+(N/starting_point)))
            else:
                starting_point -= 1

    return int(2*(N+1))


if __name__ == '__main__':
    print(solution(30))
    print(solution(1))
    print(solution(999999997))
