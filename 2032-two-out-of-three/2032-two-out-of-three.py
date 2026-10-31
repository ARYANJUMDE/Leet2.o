class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        x=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                x.append(nums1[i])
            elif nums1[i] in nums3:
                x.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                x.append(nums2[i])
            elif nums2[i] in nums3:
                x.append(nums2[i])
        for i in range(len(nums3)):
            if nums3[i] in nums1:
                x.append(nums3[i])
            elif nums3[i] in nums2:
                x.append(nums3[i])
        return list(set(x))
        
        