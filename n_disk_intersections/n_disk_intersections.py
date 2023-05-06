from bisect import bisect_right


def solution(A):
    # Extract leftmost point of each circle, together with center index
    B = []
    leftmost_start = []
    for i in range(len(A)):  # O(N)
        B.append((i - A[i], A[i]))  # (leftmost, radius). Sort by leftmost
        leftmost_start.append(i - A[i])

    B.sort()  # O(NlogN)
    leftmost_start.sort()

    # print(B)

    # circles are guaranteed to be listed sequentially on the integer line (no gaps)

    # radii = [b[1] for b in B]

    n_intersections = 0
    for i in range(len(B)):
        curr_cirle_leftmost = B[i][0]
        curr_circle_radius = B[i][1]

        # bisect(leftmost_start[i:]) causes problems with indexing
        # spot = bisect.bisect_left(leftmost_start[i+1:], curr_cirle_leftmost + (2 * curr_circle_radius) + 1)
        spot = bisect_right(leftmost_start, curr_cirle_leftmost + (2 * curr_circle_radius), lo=i+1)

        n_intersections += spot - (i+1)#max(spot - (i+1), 0)

        # for j in range(i + 1, len(B)): # This is O(N) in worst case :(
        #     # O(N**2) :(
        #     target_circle_leftmost = B[j][0]
        #     if target_circle_leftmost <= curr_cirle_leftmost + 2*curr_circle_radius:
        #         n_intersections += 1
        #     else:
        #         break

        # Search from i to j > i+2*circle_radius
        # Add j-i

        # We cannot just add 2*radius bcs multiple circles can start at the same following point (different radii)
        # n_intersections += min(2 * curr_circle_radius, len(B) - (i + 1)) # -1 bcs. not intersect with current circle

        # Handle case when radius of current circle exceeds nr. of circles on its right
        # Circles on the left will be counted because we sorted

    if n_intersections > 10000000: # 10 M
        return -1 # Edge case defined by problem defn.

    return n_intersections


if __name__ == '__main__':
    # solution([3,15,4,4,12,2,4])
    assert solution([1, 5, 2, 1, 4, 0]) == 11
