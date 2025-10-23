class Solution(object):
    def countBits(self, n):
        a = []
        for i in range(n + 1):
            temp = bin(i)[2:]
            a.append(temp.count('1'))
        return a
