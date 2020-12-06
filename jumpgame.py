class Solution(object):
    def canJump(self, nums):
        if nums==[0]:
            return True
        ans=True
        for i in range(len(nums)):
            if nums[i]==0:
                j=i-1
                ans=False
                print ans,i,j
                while j>=0 and ans==False:
                    print i,j,nums[j],(i-j)
                    if i==len(nums)-1 and nums[j]>=(i-j):
                        ans=True
                        break
                    if nums[j]>(i-j):
                        ans=True
                        break
                    j-=1
                if ans==False:
                    return False
        return ans
                    