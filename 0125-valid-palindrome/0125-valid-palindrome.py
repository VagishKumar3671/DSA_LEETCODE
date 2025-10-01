class Solution(object):
    def isPalindrome(self, s):
        if len(s)==0 or len(s)==1:
            return True
        chars = []
        for i in s:
            if i.isalnum():
                chars.append(i.lower())
        s = "".join(chars)
        first = 0
        sec = len(s) - 1
        while first < sec:
            if s[first] != s[sec]:
                return False
            first += 1
            sec -= 1
        return True
