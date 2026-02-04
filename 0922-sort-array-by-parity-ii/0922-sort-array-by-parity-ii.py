class Solution(object):
    def sortArrayByParityII(self, nums):
        # r=len(nums)//2
        # for i in range(r):
        #     if(i%2!=0 or nums[i]%2!=0):
        #         for j in range(r,2*r):
        #             nums[i],nums[j]=nums[j],nums[i]
        #             break
        # return(nums)
        odd=[]
        even=[]
        r=len(nums)
        for num in nums:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        for i in range(r):
            if i%2==0:
                nums.pop(i)
                nums.insert(i,even[0])
                even.pop(0)
            else:
                nums.pop(i)
                nums.insert(i,odd[0])
                odd.pop(0)
        return nums


        