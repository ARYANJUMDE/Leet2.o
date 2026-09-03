class Solution(object):
    def uniformArray(self, nums1):
        count=0
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                count=count+1
        if count==len(nums1):
            return True
        if min(nums1)%2==0:
            return False
        return True

        # nums1.sort()
        # count=0
        # for i in range(len(nums1)):
        #     if nums1[i]%2!=0:
        #         count=count+1
        #     if nums1[i]%2==0 and count>0:
        #         continue
        #     else:
        #         return False
        # return True
            
        