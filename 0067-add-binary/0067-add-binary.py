class Solution(object):
    def addBinary(self, a, b):
        length_max = max(len(a), len(b))
        new = ''
        a = ('0' * ((length_max + 1) - len(a))) + a
        b = ('0' * ((length_max + 1) - len(b))) + b
        car = '0'
        for i in range(1, length_max + 1):
            A = a[-i]
            B = b[-i]
            total = (A == '1') + (B == '1') + (car == '1')
            if total == 0:
                new = '0' + new
                car = '0'
            elif total == 1:
                new = '1' + new
                car = '0'
            elif total == 2:
                new = '0' + new
                car = '1'
            else:  
                new = '1' + new
                car = '1'
        if car == '1':
            new = '1' + new
        return new