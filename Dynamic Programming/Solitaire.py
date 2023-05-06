# This is the Maximal Sum problem, constrained that we can only jump up to 6 elements at a time
# You have to pass over positive numbers now for the sake of bigger positive numbers in the future

# Optimal Subsolutions? Yes, as long as subsolutions are factors of 6
# Overlapping subproblems - obviously, if > 6

# => Dynamic Programming!


# Start from last 7 numbers - these are the max reach of dice.
# Remember, we have to touch both square 0 and square N-1


def solution(A):
    # Start from A[-6:]
    # Find Max Sum solution
    # ???
    # Transition from last 7 to previous unclear.
    # I guess go back 7 from start of max sequence for last 7?

    max_sequence = []

    i = len(A)
    while i != 0:
        current_seq = A[i-7, i]

        max_sequence.append(solve_7_seq(current_seq))


def solve_7_seq(seq):
