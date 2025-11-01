class Solution(object):
    def getLucky(self, s, k):
        temp = ''
        for i in s:
            temp += str(ord(i) - ord('a') + 1)        
        for _ in range(k):
            num = 0
            for j in temp:
                num += int(j)
            temp = str(num)
        return int(temp)
