class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 1 and digits[0] == 0:
            return [1]
        digits[-1] = digits[-1] + 1
        for i in range(1, len(digits) + 1):
            if digits[-i] > 9:
                digits[-i] = 0
                if i == len(digits):
                    digits.insert(0, 1)
                else:
                    digits[-(i + 1)] = digits[-(i + 1)] + 1
            else:
                break
        return digits