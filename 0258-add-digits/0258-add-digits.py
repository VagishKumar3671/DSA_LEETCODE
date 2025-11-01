class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        while num >= 10:
            temp = 0
            while num > 0:
                digit = num % 10
                temp += digit
                num //= 10
            num = temp
        return num
