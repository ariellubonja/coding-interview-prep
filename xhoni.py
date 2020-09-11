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
    digits = [int(c[digit_pos]) for c in T]
    # number_of_groups = max(digits)

    dict = {}

    pos = 0
    while pos < len(T):
        if digits[pos] not in dict:
            dict[digits[pos]] = [R[pos]]
        else:
            dict[digits[pos]].append(R[pos])
        pos += 1

    for k in dict.keys():
        for val in dict[k]:
            if val != "OK":
                dict[k] = 0
                break
            dict[k] = 1

    score = 0
    score_per_group = int(100 / len(dict))

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