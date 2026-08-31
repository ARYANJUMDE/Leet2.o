class Solution(object):
    def minimumDeletions(self, nums):
        x=nums.index(max(nums))
        y=nums.index(min(nums))
        z=len(nums)//2
        if x>z and y<z:
            t=len(nums[:x+1])
            p=len(nums[y:])
            o=len(nums[:y+1])
            u=len(nums[x:])
            return min(t,p,o+u)
        if x<z and y>z:
            t=len(nums[:y+1])
            p=len(nums[x:])
            o=len(nums[:x+1])
            u=len(nums[y:])
            return min(t,p,o+u)
        if x!=z and y!=z and x<z and y<z:
            return(len(nums[:max(x,y)+1]))
        if x!=z and y!=z and x>z and y>z:
            return(len(nums[min(x,y):]))
        if x==z and y<z:
            return(z+1)
        if y==z and x<z:
            return z+1
        if x==z and y>z:
            return min(z+1,len(nums[x:y+1]))
        if y==z and x>z:
            return min(z+1,len(nums[y:x+1]))
        if x==z and y==z:
            return z+1