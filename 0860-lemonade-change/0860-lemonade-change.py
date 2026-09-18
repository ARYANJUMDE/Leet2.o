class Solution(object):
    def lemonadeChange(self, bills):
        five=0
        ten=0
        for i in range(len(bills)):
            if bills[i]==5:
                five=five+1
            if bills[i]==10:
                ten=ten+1
                if five!=0:
                    five=five-1
                else:
                    return False
            if bills[i]==20:
                if five!=0 and ten!=0:
                    five=five-1
                    ten=ten-1
                elif five>=3:
                    five=five-3
                else:
                    return False
        return True

        