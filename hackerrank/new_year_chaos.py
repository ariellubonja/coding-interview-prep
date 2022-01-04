# The line jumping problem

def minimumBribes(q):
    bribes = 0

    for i in range(len(q)):
        if q[i] > i + 2 + 1: # since index is 0-based
            print("Too chaotic")
            return

    for i in range(len(q)-1,0,-1):
        for j in range(max(q[i]-2,0),i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)

# # O(n^2)
# def minimumBribes(q):
#     # sorted_q = sorted(q) # O(nlogn)
#
#     chaos = 0
#
#     for i in range(len(q)): # O(n^2). Could be too slow for most test cases
#         count_swaps = 0
#         # If any element coming after i is smaller than i, that means a swap has occurred.
#         # If there are more than 2 such elements, Too Chaotic
#         for j in range(i+1, len(q)):
#             if q[i] > q[j]: # Cannot have equal
#                 count_swaps += 1
#                 if count_swaps > 2:
#                     print("Too chaotic")
#                     return
#
#         chaos += count_swaps
#
#     print(chaos)

# for i in range(len(sorted_q)-1, -1, -1):
#     if q[i] != sorted_q[i]:
#         if q[i - 1] != sorted_q[i] and q[i - 2] != sorted_q[i]: # Forward in line
#             # If current element isn't forward in queue, maybe it's behind
#             if i + 2 < len(q): # If a person accepted a bribe, they can be at most 2 behind, but they cannot wrap
#                 # around to the front of the queue
#                 if q[i + 1] != sorted_q[i] and q[i + 2] != sorted_q[i]: # Backwards in line
#                     # Wrapping around doesn't make sense here because nobody will bribe to go back in line
#                     print("Too chaotic")
#                     return
#             elif i + 1 < len(q):
#                 if q[i + 1] != sorted_q[i]:
#                     print("Too chaotic")
#                     return
#             else:
#                 print("Too chaotic")
#                 return
#             # Else, things are fine. don't do anything
#         elif q[i - 1] == sorted_q[i]:
#             chaos += 1
#         else: # Is there another case?
#             chaos += 2

if __name__ == '__main__':
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
