class Solution(object):
    def hammingDistance(self, x, y):
        if x == y:
            return 0
        if x == 0 or y == 0:
            return bin(x or y)[2:].count('1')
        binary_x = bin(x)[2:]
        binary_y = bin(y)[2:]
        max_len = max(len(binary_x), len(binary_y))
        binary_x = binary_x.zfill(max_len)
        binary_y = binary_y.zfill(max_len)
        count = 0
        for i in range(max_len):
            if binary_x[i] != binary_y[i]:
                count += 1
        return count
