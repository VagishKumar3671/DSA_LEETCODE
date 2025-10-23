class Solution(object):
    def reverseBits(self, n):
        temp = bin(n)[2:]  
        return int((('0' * (32 - len(temp))) + temp)[::-1], 2)