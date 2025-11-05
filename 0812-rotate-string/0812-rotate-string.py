class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        return False