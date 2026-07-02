class Solution(object):
    def subarraySum(self, nums, k):
        # count=0
        # z=[]
        # t=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         z.append(nums[i:j])
        # for i in range(len(z)):
        #     t.append(sum(z[i]))         
        # return(t.count(k))
        count=0
        x=[nums[0]]
        for i in range(1,len(nums)):
            x.append(x[-1]+nums[i])

# x=[1,3,4,6,7]

# suppose we are at index 3 ie 6 and we want a subarray whose sum is 3
# now we need to subtract some number from 6 to get 3 ie we need to subtract 3
# from 6 to get target so have we seen 3 before 6 ie Yes so there exists a subarray
        hashmap={0:1}
        for i in range(len(x)):
            if x[i]-k in hashmap:
                count=count+hashmap[x[i]-k]
            if x[i] in hashmap:
                hashmap[x[i]]=hashmap[x[i]]+1
            else:
                hashmap[x[i]]=1
        return(count)            