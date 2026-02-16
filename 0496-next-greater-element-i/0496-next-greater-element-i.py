class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        x=[]
        for num in nums1:
            if num in nums2:
                t=nums2.index(num)
            for i in range(t,len(nums2)):
                if nums2[i]>num:
                    x.append(nums2[i])
                    break
            else:
                x.append(-1)
        
        return(x)
        