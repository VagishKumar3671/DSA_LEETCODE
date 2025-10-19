class Solution(object):
    def titleToNumber(self, columnTitle):
        dic = {chr(i + 65): i+1 for i in range(26)}
        if len(columnTitle)==1:return dic[columnTitle]
        num=0
        for i in range(1,len(columnTitle)+1):
            temp = columnTitle[-i]
            num += dic[temp] * (26 ** (i-1))
        return num