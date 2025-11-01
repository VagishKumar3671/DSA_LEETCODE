class Solution(object):
    def arrangeCoins(self, n):
        '''if n == 1:
            return 1
        fin_num = 1
        for i in range(1, n + 1):
            if n >= fin_num:
                n -= fin_num
                fin_num += 1
            else:
                return i - 1
        return i'''
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            coins = (mid * (mid + 1)) // 2 
            if coins > n:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        return res