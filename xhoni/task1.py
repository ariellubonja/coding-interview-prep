# Task 1: Nathan's number of points
# T = ["test1a",
#     "test2",
#     "test1b",
#     "test1c",
#     "test3",
#     ]

# R = [ "Wrong Answer",
#     "OK",
#     "Runtime error",
#     "OK",
#     "Time limit exceeded"
# ]

# Points given only if every test case in group was OK

def solution(T, R):
    # Find the position of the number
    digit_pos = [i for i in range(len((T[0]))) if T[0][i].isdigit()][0]

    # Find the number of test groups
    # digits = [int(c[digit_pos]) for c in T]
    # number_of_groups = max(digits)

    dict = {}

    T_pos = 0
    # Populate dictionary
    while T_pos < len(T):
        if int(T[T_pos][digit_pos]) not in dict:
            dict[int(T[T_pos][digit_pos])] = [R[T_pos]]
        else:
            dict[int(T[T_pos][digit_pos])].append(R[T_pos])
        T_pos += 1

    for k in dict.keys():
        for val in dict[k]:
            if val != "OK":
                dict[k] = False
                break
            dict[k] = True

    score = 0
    score_per_group = int(100 / len(dict))

    # score += []

    for val in dict.values():
        if val == 1:
            score += score_per_group

        # Map scores to this group

    # If group is full of OK, we count it

    return score


if __name__ == '__main__':
    print(solution(["test1a",
                    "test2",
                    "test1b",
                    "test1c",
                    "test3",
                    ]
                   ,
                   [ "Wrong Answer",
                     "OK",
                     "Runtime error",
                     "OK",
                     "Time limit exceeded"
                     ]
                   ))

    print(solution(["codility1",
                    "codility3",
                    "codility2",
                    "codility4b",
                    "codility4a",
                    ]
                   ,
                   [ "Wrong Answer",
                     "OK",
                     "OK",
                     "Runtime error",
                     "OK"
                     ]
                   ))

    print(solution(["codility1",
                    ]
                   ,
                   [
                     "OK"
                     ]
                   ))