class Solution(object):
    def intToRoman(self, num):
        res=''
        while(num!=0):
            if num>=1000:
                res+=(num//1000)*'M'
                num%=1000
            elif num>=100:
                if num//100==9:
                    res+='CM'
                    num-=900
                    continue
                elif num >= 500:
                    res += "D"
                    num -= 500
                    continue
                elif num // 100 == 4:
                    res += "CD" 
                    num -= 400
                    continue
                else:
                    res+=(num//100)*'C'
                    num=num%100
            elif num >= 10:
                if num // 10 == 9:
                    res += "XC" 
                    num -= 90
                    continue
                elif num >= 50:
                    res += "L"
                    num -= 50
                    continue
                elif num // 10 == 4:
                    res += "XL" 
                    num -= 40
                    continue
                res += "X" * (num // 10)
                num = num % 10

            elif num >= 1:
                if num // 1 == 9:
                    res += "IX" 
                    num -= 9
                    continue
                elif num >= 5:
                    res += "V"
                    num -= 5
                    continue
                elif num // 1 == 4:
                    res += "IV" 
                    num -= 4
                    continue
                res += "I" * num
                num = 0
        return res
        