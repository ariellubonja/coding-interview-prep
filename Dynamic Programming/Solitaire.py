# This is the Maximal Sum problem, constrained that we can only jump up to 6 elements at a time
# You have to pass over positive numbers now for the sake of bigger positive numbers in the future

# Optimal Subsolutions? Yes, as long as subsolutions are factors of 6
# Overlapping subproblems - obviously, if > 6

# => Dynamic Programming!


# Start from last 7 numbers - these are the max reach of dice.
# Remember, we have to touch both square 0 and square N-1
from copy import deepcopy


def solution(A):
    a = solve_sequence(A, A[len(A) - 1])
    if A[0] < 0:
        a += A[0] # Need to add starting point. It wasn't added if negative
    return a



# TODO Add limit of 6-sided die jumps
def solve_sequence(seq, current_sum):
    # whether_to_add_curr + min(subsequence)
    if len(seq) == 0:
        return 0
    elif len(seq) == 1:
        return seq[0]
    else:
        subseq = seq[max(len(seq)-7, 0):-1] # Exclude last element - it has to be added anyway
        start_index, ss_sum = solve_6_subseq(subseq)
        # ss_sum += seq[len(seq) - 1] # Add last element to sum

        current_sum += ss_sum

        start_index += max(len(seq)-7, 0) # start_index doesn't correspond to position in A. Make it so

        subseq = seq[:start_index + 1]

        current_sum += solve_sequence(subseq, current_sum)

    return current_sum

        # if seq[0] > 0:
        #     return seq[0] + solve_subsequence(seq[1:])
        # else:
        #     return solve_subsequence(seq[1:])

def solve_6_subseq(seq):
    # Find minimum sum in this sequence
    argmaxes = []
    currSum = 0
    MIN_INT = -9223372036854775807 # Python3 doesn't have a min int but close enough
    prevSum = MIN_INT

    newseq = seq.copy()
    while len(newseq) > 0:
        # Find max elements of the current sequence, in order from biggest to least
        ss_max = max(newseq)

        currSum += ss_max

        if prevSum >= currSum:
            break

        argmaxes.append(seq.index(ss_max))
        newseq.remove(ss_max)
        prevSum = deepcopy(currSum) # update prevSum to match


    return min(argmaxes), prevSum # Max Sum and starting location





# https://stackoverflow.com/questions/16945518/finding-the-index-of-the-value-which-is-the-min-or-max-in-python
def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]


if __name__ == '__main__':
    # assert solution([1, -2, 0, 9, -1, -2]) == 8
    # assert solution([-4, -10, -7]) == -11
    assert solution([0, -4, -5, -2, -7, -9, -3, -10]) == -12