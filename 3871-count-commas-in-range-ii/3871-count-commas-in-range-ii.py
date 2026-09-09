class Solution(object):
    def countCommas(self, n):
        p=str(n)
        if len(p)<4:
            return 0
        else:
            if len(p)<=6:
                return n-1000+1
            else:
                t=999999-1000+1
                count1=0
                count2=0
                for i in range(7,17):
                    if len(str(n))==i:
                        count2=count2+(n-(10**(i-1))+1)*((i-1)//3)
                        count2=count2+count1+t
                        return count2
                    if len(str(n))>i:
                        count1=count1+(9*(10)**(i-1))*((i-1)//3)
                    

                


        