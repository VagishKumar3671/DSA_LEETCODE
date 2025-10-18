class Solution(object):
    def addBinary(self, a, b):
        length_max,new,car = max(len(a),len(b)),'','0'
        a,b = ('0' * ((length_max + 1) - len(a))) + a,('0' * ((length_max + 1) - len(b))) + b
        for i in range(1, length_max + 1):
            total = (a[-i] == '1') + (b[-i] == '1') + (car == '1')
            if total == 0:new,car = '0' + new,'0'
            elif total == 1:new,car = '1' + new,'0'
            elif total == 2:new,car= '0' + new,'1'
            else:new,car = '1' + new,'1'
        if car == '1':
            new = '1' + new
        return new