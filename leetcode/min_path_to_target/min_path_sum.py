# non-negative nr. case satisfies triangle inequality => DP
# DP matrix sln
class Solution:
    best_path = 0
    prev_positions = []
    memo = {}

    def is_valid(self, grid, i, j):
        # check whether position is in-bounds and not previously visited
        # TODO pretty sure prev_positions and memo are not both needed
        return not (i < 0 or j < 0 or (i, j) in self.prev_positions)

    def min_path_helper(self, grid, i, j):
        # Base Case 2x2
        # TODO deal w/ edge cases
        if i == 0 and j == 0:
            return grid[0][0]

        if (i, j) in self.memo:
            return self.memo[(i, j)]

        # can only move right or up going backwards. problem says so
        possible_mins = []
        if i - 1 >= 0:
            possible_mins.append(self.min_path_helper(grid, i - 1, j))
        if j - 1 >= 0:
            possible_mins.append(self.min_path_helper(grid, i, j - 1))
        # if self.is_valid(grid, i+1,j):
        #     prev_dirs.append(self.min_path_helper(grid, i+1,j))
        #     self.prev_positions.append((i+1, j))
        # if self.is_valid(grid, i,j+1):
        #     prev_dirs.append(self.min_path_helper(grid, i,j+1))
        #     self.prev_positions.append((i, j+1))

        best = grid[i][j] + min(possible_mins)
        self.memo[(i, j)] = best
        return best

    def minPathSum(self, grid: list[list[int]]) -> int:
        # Without this, Leetcode remembers state from last problem, giving wrong sln!
        # WTF
        self.best_path = 0
        self.prev_positions = []
        self.memo = {}

        i = len(grid) - 1
        j = len(grid[0]) - 1

        return self.min_path_helper(grid, i, j)


# if __name__ == '__main__':
#     sln = Solution()
#
#     # grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
#     # print(sln.minPathSum(grid))
#
#     grid = [[1, 2, 3], [4, 5, 6]]
#     print(sln.minPathSum(grid))


if __name__ == '__main__':
    sln = Solution()

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sln.minPathSum(grid))

    grid = [[1, 2, 3], [4, 5, 6]]
    print(sln.minPathSum(grid))
