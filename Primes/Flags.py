# N in [1, 400k]
# n in [0, 1B]

def solution(A):
    if len(A) < 3:
        return 0
    # Find nr of peaks, easy O(N), if A[-1], A[+1] is smaller
    peaks = []
    i = 1
    while i < len(A) - 1:
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)
            # Skip i forward by 2, because if current index is peak, curr + 1 is definitely not
            i += 1
        i += 1

    if len(peaks) <= 2:
        return len(peaks)
    # Return max nr of flags. We can put a flag every more than or equal to -nr-of-flags- distance
    #   This can be done in O(nr-of-peaks)
    flag_positions = [peaks[0]]
    max_flags = 1
    for num_flags in range(len(peaks), 1, -1):
        for peak in peaks[1:]:
            if peak - flag_positions[-1] >= num_flags:
                flag_positions.append(peak)
                max_flags = max(max_flags, len(flag_positions))
        # No sense to keep going all the way down if we already have equal or less flags than planted
        if num_flags <= max_flags:
            return max_flags

    # TODO How do primes relate to this??

    return max_flags


if __name__ == '__main__':
    print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))
    print(solution([1]))
    print(solution([0, 0, 0, 0, 0, 1, 0, 1, 0, 1]))
