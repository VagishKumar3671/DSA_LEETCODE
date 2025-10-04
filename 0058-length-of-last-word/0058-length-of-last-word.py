class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s)==0 or len(s)==1:
            return len(s)
        return len(s.split()[-1])
