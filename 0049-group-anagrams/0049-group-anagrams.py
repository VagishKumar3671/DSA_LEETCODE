class Solution(object):
    def map(self,x):
        count=[0]*26
        for j in x:
            count[ord(j)-ord('a')]+=1
        return tuple(count)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res={}
        for i in strs:
            count=self.map(i)
            if count in res:
                res[count].append(i)
                continue
            else:
                res[count]=[i]
        return list(res.values())
            