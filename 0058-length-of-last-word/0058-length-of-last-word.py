class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s)==0:
            return 0
        var=list(s.split(" "))
        n=1
        while(True):
            if(len(var[-n])==0):
                n+=1
                continue
            else:
                return len(var[-n])