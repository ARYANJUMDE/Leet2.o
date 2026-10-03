class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        count=0
        max_size=0
        for i in range(len(boxTypes)):
            count=count+boxTypes[i][0]
            if count<=truckSize:
                max_size=max_size+boxTypes[i][0]*boxTypes[i][1]
            else:
                count=count-boxTypes[i][0]
                diff=truckSize-count
                max_size=max_size+diff*boxTypes[i][1]
                break
        return(max_size)
        

#         boxTypes.sort(reverse=True,key=lambda boxTypes:boxTypes[1])
#         self.total_unit=0
#         for self.boxcount,self.unitperbox in boxTypes:
#             if(truckSize>=self.boxcount):
#                 self.total_unit=self.total_unit+self.boxcount*self.unitperbox
#                 truckSize=truckSize-self.boxcount
#             else:
#                 self.total_unit=self.total_unit+truckSize*self.unitperbox
#                 break
#         return self.total_unit
# s=Solution()
# s.maximumUnits([[1,3],[2,2],[3,1]],4)
