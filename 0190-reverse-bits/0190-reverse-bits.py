class Solution(object):
    def reverseBits(self, n):
        temp = bin(n)[2:]
        temp = (('0' * (32 - len(temp))) + temp)[::-1]  
        return int(temp, 2)