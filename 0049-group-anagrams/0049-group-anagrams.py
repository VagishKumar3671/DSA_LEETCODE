class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res={}
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            count=tuple(count)
            if count in res:
                res[count].append(i)
                continue
            else:
                res[count]=[i]
        return list(res.values())
            