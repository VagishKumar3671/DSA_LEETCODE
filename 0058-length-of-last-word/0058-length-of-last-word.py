class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s)==0:
            return 0
        return len(s.split()[-1])
