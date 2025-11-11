class Solution(object):
    def wordPattern(self, pattern, s):
        lis1 = s.split(" ")
        if len(lis1) != len(pattern):
            return False
        dic = {}
        for i in range(len(lis1)):
            word = lis1[i]
            ch = pattern[i]
            if ch in dic:
                if dic[ch] != word:
                    return False
            else:
                if word in dic.values():
                    return False
                dic[ch] = word 
        return True
