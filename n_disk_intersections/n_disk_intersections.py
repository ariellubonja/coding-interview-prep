def solution(A):
    # Extract leftmost point of each circle, together with center index
    B = []
    for i in range(len(A)):  # O(N)
        B.append((i - A[i], A[i]))  # (leftmost, radius)

    B.sort()  # O(NlogN)

    # print(B)

    # circles are guaranteed to be listed sequentially on the integer line (no gaps)

    n_intersections = 0
    for i in range(len(B)):
        curr_circle_radius = B[i][1]

        for j in range(i + 1, len(B)): # This is O(N) in worst case :(
            if B[j][0] <= B[i][0] + 2*curr_circle_radius:
                n_intersections += 1
            else:
                break


        # We cannot just add 2*radius bcs multiple circles can start at the same following point (different radii)
        # n_intersections += min(2 * curr_circle_radius, len(B) - (i + 1)) # -1 bcs. not intersect with current circle

        # Handle case when radius of current circle exceeds nr. of circles on its right
        # Circles on the left will be counted because we sorted

    return n_intersections


if __name__ == '__main__':
    assert solution([1, 5, 2, 1, 4, 0]) == 11
