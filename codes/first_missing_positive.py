class Solution(object):
    def firstMissingPositive(self, nums):
        d={}
     
        for  i in nums:
            d[i]=1
        m=1
        while True:
            try:
                if d[m]:
                    m+=1
            except KeyError:
                break
        return m
            