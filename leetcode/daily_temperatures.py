from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # TODO this can clearly be done in linear time with using Stacks
        # TODO think of this like the Bracket matching problem:
        # TODO warm: (, warmer: )

        stackinator = []
        # Init. to 0
        days_to_wait = [0 for t in temperatures]

        for curr_date in range(len(temperatures)):
            curr_temp = temperatures[curr_date]

            if not stackinator:
                stackinator.append(curr_date)
            else:
                # by definition, temperatures in the stack must be descending
                # If they were increasing, they would have been popped
                while stackinator:
                    past_date = stackinator[-1]
                    # print("curr_temp: ", curr_temp)
                    past_temp = temperatures[past_date]

                    # print("past_temp: ", past_temp)

                    if curr_temp > past_temp:
                        stackinator.pop()
                        days_to_wait[past_date] = curr_date - past_date
                    else:
                        break
                
                stackinator.append(curr_date)
        
        return days_to_wait
                        



