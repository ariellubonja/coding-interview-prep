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
    max_sum = 0
    while i != 0:
        start = max(i-7, 0)
        current_seq = A[start:i]

        sol_seq, seq_sum = solve_7_seq(A, current_seq)
        max_sequence.insert(0, sol_seq) # Insert list at start of current
        i = sol_seq[0]
        max_sum += seq_sum


    return max_sum


def solve_7_seq(A, seq):
    # [1, -2, 0, 9, -1, -2]
    # Sln: 0, 3, 2 - dice roll

    sln_path = []
    maxSum = 0
    for i in range(len(seq) - 1):
        # If number ahead is positive, add to solution
        if A[i] > 0:
            sln_path.append(i)
            maxSum += A[i]

    sln_path.append(len(seq) - 1)  # We need to get to the last element of the current sequence to "exit" the game

    maxSum += A[len(seq) - 1]

    return sln_path, maxSum


if __name__ == '__main__':
    assert solution([1, -2, 0, 9, -1, -2]) == 8