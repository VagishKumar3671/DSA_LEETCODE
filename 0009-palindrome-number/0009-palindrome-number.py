class Solution:
    def isPalindrome(self, x):
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        temp = x
        while temp > 0:
            reversed_num = reversed_num * 10 + temp % 10
            temp //= 10

        return x == reversed_num
