class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        
        # Variables to store the best palindrome found
        longest = s[0]  # at least one character will always be a palindrome
        
        # Check all possible centers (i..j)
        for i in range(len(s)):
            j = len(s) - 1
            while j >= i:
                if s[i] == s[j]:
                    # check substring s[i:j+1]
                    sub = s[i:j+1]
                    if sub == sub[::-1]:  # palindrome check
                        if len(sub) > len(longest):
                            longest = sub
                j -= 1
                
        return longest
