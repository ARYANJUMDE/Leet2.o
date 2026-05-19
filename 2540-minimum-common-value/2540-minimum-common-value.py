class Solution(object):
    def getCommon(self, nums1, nums2):
        nums2=set(nums2)
        for num in nums1:
            if num in nums2:
                return(num)
        return -1


        