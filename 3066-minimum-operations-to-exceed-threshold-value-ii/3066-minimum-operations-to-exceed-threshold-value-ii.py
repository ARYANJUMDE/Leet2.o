class Solution(object):
    def minOperations(self, nums, k):
        count=0
        # while all(num>=k for num in nums)==False:
        #     min_num1=min(nums)
        #     nums.remove(min_num1)
        #     min_num2=min(nums)
        #     nums.remove(min_num2)

        #     nums.append(min(min_num1,min_num2)*2+max(min_num1,min_num2))
        #     count=count+1
        # return(count)
        
        # nums.sort()
        # i=0
        # while i<len(nums) and nums[i]<k:
        #     min1=nums[i]
        #     min2=nums[i+1]
        #     i=i+2
        #     new_val=min1*2+min2
        #     nums.append(new_val)
        #     nums.sort()
        #     count=count+1
        # return count
        heapq.heapify(nums)
        while nums[0]<k:
            min1=heapq.heappop(nums)
            min2=heapq.heappop(nums)
            new=min1*2+min2
            heapq.heappush(nums,new)
            count=count+1
        return(count)
