class Solution(object):
    def reverseWords(self, s):
        # x=s.split()
        # x.reverse()
        # t=""
        # for i in range(len(x)):
        #     t=t+x[i]
        #     if i != len(x) - 1:
        #         t += " "
        
        # return(t)
        x=s.split()
        
        return(' '.join(x[::-1]))

        