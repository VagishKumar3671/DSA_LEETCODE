class Solution(object):
    def combine(self, temp1, temp2):
        temp = []
        for i in temp1:
            for j in temp2:
                temp.append(i + j)
        return temp
    def letterCombinations(self, digits):
        if len(digits) == 0 or (len(digits) == 0 and digits[0]=='1') or (len(digits) == 0 and digits[0]=='0'):
            return []
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if len(digits) == 1:
            return dic[digits[0]]
        temp1 = dic[digits[0]]
        for i in range(1, len(digits)):
            temp2 = dic[digits[i]]
            temp1 = self.combine(temp1, temp2)
        return temp1
