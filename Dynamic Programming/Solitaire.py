# This is the Maximal Sum problem, constrained that we can only jump up to 6 elements at a time
# You have to pass over positive numbers now for the sake of bigger positive numbers in the future

# Optimal Subsolutions? Yes, as long as subsolutions are factors of 6
# Overlapping subproblems - obviously, if > 6

# => Dynamic Programming!


# Start from last 7 numbers - these are the max reach of dice.
# Remember, we have to touch both square 0 and square N-1


def solution(A):
    a = solve_subsequence(A)
    if A[0] < 0:
        a += A[0] # Need to add starting point. It wasn't added if negative
    return a
    # Start from A[-6:]
    # Find Max Sum solution
    # ???
    # Transition from last 7 to previous unclear.
    # I guess go back 7 from start of max sequence for last 7?
    #
    # max_sequence = []
    #
    # i = len(A)
    # max_sum = 0
    # while i != 0:
    #     start = max(i-7, 0)
    #     current_seq = A[start:i]
    #
    #     sol_seq, seq_sum = solve_7_seq(A, current_seq)
    #     max_sequence.insert(0, sol_seq) # Insert list at start of current
    #     i = sol_seq[0]
    #     max_sum += seq_sum
    # return max_sum




# TODO Add limit of 6-sided die jumps
def solve_subsequence(seq):
    # whether_to_add_curr + min(subsequence)
    if len(seq) == 1:
        return seq[0]
    else:
        if seq[0] > 0:
            return seq[0] + solve_subsequence(seq[1:])
        else:
            return solve_subsequence(seq[1:])



if __name__ == '__main__':
    assert solution([1, -2, 0, 9, -1, -2]) == 8
    assert solution([-4, -10, -7]) == -11
    assert solution([0, -4, -5, -2, -7, -9, -3, -10]) == -12