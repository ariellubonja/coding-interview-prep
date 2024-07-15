class Solution:

    def recursive_helper(self, short_cost: list[int], memo):
        # return cost to n. This means we need to add a placeholder for the top of the stair

        n = len(short_cost) - 1  # index of last pos
        if n in memo:
            return memo[n]
        else:
            curr_min = min(self.recursive_helper(short_cost[:len(short_cost) - 2], memo),
                           self.recursive_helper(short_cost[:len(short_cost) - 1], memo)) + short_cost[-1]
            memo[n] = curr_min
            return curr_min

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)  # placeholder for top of stair
        memo = {}
        memo[0] = cost[0]
        memo[1] = cost[1]

        return self.recursive_helper(cost, memo)
        total_cost = []
        # Base Case
        if len(cost) == 2:
            return min(cost)
        else:
            # Base Case
            if cost[0] < cost[1]:
                total_cost.append(cost[0])
                skipNext = False
            else:
                total_cost.append(cost[1])
                skipNext = True

            for i in range(1, len(cost) - 1):
                if skipNext:
                    skipNext = False
                    continue

                print(total_cost)
                print(i)

                if cost[i] < cost[i + 1]:
                    total_cost.append(total_cost[-1] + cost[i])
                    skipNext = False
                else:
                    total_cost.append(total_cost[-1] + cost[i + 1])
                    skipNext = True

            return total_cost[-1]


if __name__ == '__main__':
    sln = Solution()
    cost = [10,15,20]
    print(sln.minCostClimbingStairs(cost))

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(sln.minCostClimbingStairs(cost))