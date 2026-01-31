class Solution(object):
    def nextGreatestLetter(self, letters, target):
        x=[]
        for i in range(len(letters)):
            x.append(letters[i])
        heapq.heapify(letters)
        while len(letters)>0:
            if letters[0]>target:
                return(letters[0])

            else:
                heapq.heappop(letters)
        return x[0]
        