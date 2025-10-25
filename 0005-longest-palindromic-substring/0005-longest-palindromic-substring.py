class Solution(object):
    def repect_checker(self, s):
        for ch in s:
            if s.count(ch) > 1:
                return True
        return False
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        if not self.repect_checker(s):
            return ""  
        longest = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1] and len(sub) > len(longest):
                    longest = sub
        return longest
