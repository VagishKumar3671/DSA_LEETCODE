class Solution(object):
    def maxArea(self, height):
        if (len(height)==2):
            return min(height[0],height[1])*(1)
        l,r,max_ans=0,len(height)-1,0
        while l<r:
            max_ans=max((min(height[l],height[r])*(r-l)),max_ans)
            if height[l]>=height[r]:
                r-=1
            else:
                l+=1
        return max_ans


        