class Solution(object):
    def minBitFlips(self, start, goal):
        if start == goal:
            return 0
        start_binary = bin(start)[2:]
        goal_binary = bin(goal)[2:]
        max_len = max(len(start_binary), len(goal_binary))
        start_binary = start_binary.zfill(max_len)
        goal_binary = goal_binary.zfill(max_len)
        change = 0
        for i in range(max_len):
            if start_binary[i] != goal_binary[i]:
                change += 1
        return change
