class Solution(object):
    def isTrionic(self, nums):
        # count1=0
        # count2=0
        # if nums[0]<nums[1]:
        #     for i in range(0,len(nums)-1):
        #         if nums[i]<nums[i+1]:
        #             count1=count1+1
        #         else:
        #             break
        #     for i in range(i,len(nums)-1):
        #         if nums[i]>nums[i+1]:
        #             count2=count2+1
        #         else:
        #             break
        #     for i in range(i,len(nums)-1):
        #         if nums[i]<nums[i+1]:
        #             count1=count1+1
        #         else:
        #             break
        # if count1+count2+1==len(nums):
        #     return True
        # return False
        count1=0
        count2=0
        count3=0
        for i in range(0,len(nums)-1):
            if nums[i]<nums[i+1]:
                count1=count1+1
            else:
                break
        if count1>0:
            for i in range(i,len(nums)-1):
                if nums[i]>nums[i+1]:
                    count2=count2+1
                else:
                    break
        else:
            return False
        if count1>0 and count2>0:
            for i in range(i,len(nums)-1):
                if nums[i]<nums[i+1]:
                    count3=count3+1
                else:
                    break
        else:
            return False
        if count1>0 and count2>0 and count3>0:
            if count1+count2+count3+1==len(nums):
                return True
        return False


