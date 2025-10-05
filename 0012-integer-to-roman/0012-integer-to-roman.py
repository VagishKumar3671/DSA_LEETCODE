class Solution(object):
    def intToRoman(self, num):
        vals,syms,res = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"],''
        for i in range(len(vals)):
            res += (num // vals[i]) * syms[i]
            num %= vals[i]
        return res