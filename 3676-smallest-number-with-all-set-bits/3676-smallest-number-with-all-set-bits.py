class Solution(object):
    def smallestNumber(self, n):
        binary = bin(n)[2:]
        if '0' in binary:
            return int(len(binary) * '1',2)
        else:
            return int(binary,2)
