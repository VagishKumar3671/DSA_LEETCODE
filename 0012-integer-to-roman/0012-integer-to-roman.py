class Solution(object):
    def intToRoman(self, num):
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ''
        for i in range(len(vals)):
            res += (num // vals[i]) * syms[i]
            num %= vals[i]
        return res