class Solution(object):
    def findDifference(self, nums1, nums2):
        result1=[]
        result2=[]
        x=[]
        for num in nums1:
            if num not in nums2:
                if num not in result1:
                    result1.append(num)
        for num in nums2:
            if num not in nums1:
                if num not in result2:

                    result2.append(num)
        x.append(result1)
        x.append(result2)
        
        return(x)