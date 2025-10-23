class Solution(object):
    def reverseBits(self, n):  
        return int((('0' * (32 - len(bin(n)[2:]))) + bin(n)[2:])[::-1], 2)