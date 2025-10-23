class Solution(object):
    def reverseBits(self, n):
        temp = (('0' * (32 - len(bin(n)[2:]))) + bin(n)[2:])[::-1]  
        return int(temp, 2)