class Solution(object):
    def productExceptSelf(self, nums):
        if 0 not in nums:
            t=1
            x=[]
            for i in range(len(nums)):
                t=t*nums[i]
            for i in range(len(nums)):
                x.append(t//nums[i])
            return x
        else:
            t=1
            count=0
            y=[]
            for i in range(len(nums)):
                if nums[i]!=0:
                    t=t*nums[i]
                else:
                    count=count+1
            if count==1:
                for i in range(len(nums)):
                    if nums[i]==0:
                        y.append(t)
                    else:
                        y.append(0)
            else:
                y=[0]*len(nums)
                
            return y

            
        # import math
        # x=[]
        # for i in range(0,len(nums)):
        #     t=nums.pop(nums[i])
        #     y=math.prod(nums)
        #     x.append(y)
        # nums.insert(i,t)
        
        
        # return(x)

        