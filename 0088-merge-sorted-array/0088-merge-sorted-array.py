class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2[:n])

        '''i,j=0,0
        temp=[]
        while(m>=i or n>=j):
            if nums1[i]>=nums[j]:
                temp.append(nums[j])
                j+=1
            else:
                temp.append(nums[i])
                i+=1'''
        