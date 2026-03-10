class Solution(object):
    def search(self, nums, target):
        nums=list(set(nums))
        nums.sort()
        min1=0
        max1=len(nums)-1
        while min1<=max1:
            mid=(min1+max1)//2
            if nums[mid]==target:
                return(True)
            elif (nums[mid]<target):
                min1=mid+1
            else:
                max1=mid-1
        return False

        