class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count=0
        if ruleKey=="color":
            for i in range(len(items)):
                if ruleValue==items[i][1]:
                    count=count+1
            return count
        elif ruleKey=="type":
            for i in range(len(items)):
                if ruleValue==items[i][0]:
                    count=count+1
            return count
        else:
            for i in range(len(items)):
                if ruleValue==items[i][2]:
                    count=count+1
            return count
        