class Solution(object):
    def lengthOfLastWord(self, s):
        if(len(s)==0):
            return 0
        words = s.split()
        return len(words[-1])
