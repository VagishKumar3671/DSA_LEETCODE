class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        else:
            for i in set(s):
                if s.count(i)!=t.count(i):
                    return False
                    break
            else:
                return True