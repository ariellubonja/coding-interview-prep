from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ### This solution is pretty basic, O(n^2). 
        # Alternatively, we can have a histogram of temperature indices. So, when we look at 73, look at 74+ for the min index. Advantage: can form these stacks ahead of time. Disadvantage, O(n) worst case

        ####### But, as I progress through i, I can pop these stacks off. This way, work diminishes linearly w/ i

        ### Complexity: O(nlogn) to form histogram, O(n) to find the num

        # Create a histogram (dict) of temperatures, with indices in the saved list
        temps_indices = {}
        max_temp = 29 # Min temp will be 30

        # Create dictionary of {temperature: days_with_that_temp}
        for i in range(len(temperatures)):
            t_i = temperatures[i]
            max_temp = max(max_temp, t_i)

            # Form dict, append. Each list in incrementing order
            if temps_indices.get(t_i) is None:
                temps_indices[t_i] = deque([i])
            else:
                temps_indices[t_i].append(i)

        
        # Output target
        days_till_warmer_list = []
        n_days = len(temperatures)

        for current_day in range(n_days):
            day_temp = temperatures[current_day]
            closest_warmer_day = len(temperatures) + 1

            if day_temp == max_temp: # If this day is hottest on record, return 0 and skip
                days_till_warmer_list.append(0)
                continue

            # For all warmer temperatures, look through the dictionary of indices
            for warmer_temp in range(day_temp+1, max_temp+1):
                days_w_that_temp = temps_indices.get(warmer_temp)

                if days_w_that_temp is None or len(days_w_that_temp) == 0:
                    continue
                # print("days_w_that_temp: ", days_w_that_temp)
                # print("days_w_that_temp[0]: ", days_w_that_temp[0])

                # If we've already passed day i, skip/pop those
                while len(days_w_that_temp) > 0 and current_day >= days_w_that_temp[0]:
                    # print("current_day: ", current_day)
                    # print("days_w_that_temp.popleft() :", days_w_that_temp.popleft())
                    days_w_that_temp.popleft()

                # After idx > i, then this is by definition a warmer, later day.
                # We don't know if it's the earliest one yet, bcs. there are many different temperature options
                if len(days_w_that_temp) > 0:
                    
                    closest_warmer_day = min(days_w_that_temp[0], closest_warmer_day)
            
            n_days_till_warmer = closest_warmer_day - current_day

            # If no warmer day was found, return 0
            if closest_warmer_day == len(temperatures) + 1:
                n_days_till_warmer = 0

            days_till_warmer_list.append(n_days_till_warmer)
        
        return days_till_warmer_list

            