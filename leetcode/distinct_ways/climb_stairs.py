class Solution:
    memo = {}

    def climb_stairs_helper(self, current_stair):
        # Base Case
        if current_stair == 0:
            return 0
        elif current_stair == 1:
            return 1
        elif current_stair == 2:
            return 2

        if current_stair in self.memo:
            return self.memo[current_stair]

        # Main Case, i >= 2
        else:
            sln = self.climb_stairs_helper(current_stair - 1) + self.climb_stairs_helper(current_stair - 2)
            self.memo[current_stair] = sln

            return sln

    def climbStairs(self, n: int) -> int:
        return self.climb_stairs_helper(n)
