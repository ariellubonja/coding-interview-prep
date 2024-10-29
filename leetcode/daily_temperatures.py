class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Days till warmer weather i.e. next peak/max
        # Hint: use a Stack

        # No no this is all wrong, we only want future temps, not previous. Can't sort

        days = []
        for i in range(len(temperatures)-1):
            t_i = temperatures[i]

            days_to_wait = 1
            for j in range(i+1, len(temperatures)):
                t_j = temperatures[j]

                if t_j > t_i:
                    break
                
                days_to_wait += 1
                
                if j == len(temperatures) - 1:
                    days_to_wait = 0  # When next warmer day can't be found
            
            
            days.append(days_to_wait)
        
        days.append(0) # Edge case, last element

        return days

    
### This solution is pretty basic, O(n^2). 
# Alternatively, we can have a histogram of temperature indices. So, when we 
# look at 73, look at 74+ for the min index. Advantage: can form these stacks ahead of time. Disadvantage, O(n) worst case

####### But, as I progress through i, I can pop these stacks off. This way, work diminishes linearly w/ i

### Complexity: O(nlogn) to form histogram, O(n) to find the num