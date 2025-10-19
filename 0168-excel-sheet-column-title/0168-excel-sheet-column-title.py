class Solution(object):
    def convertToTitle(self, columnNumber):
        dic = {i + 1: chr(65 + i) for i in range(26)}
        if columnNumber <= 26:
            return dic[columnNumber]
        string = ''
        while columnNumber > 0:
            rem = columnNumber % 26
            if rem == 0:
                rem = 26
            string = dic[rem] + string
            columnNumber = (columnNumber - rem) // 26
        return string
