class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        x=[]
        count2=0
        for i in range(len(words)):
            count1=0
            for j in range(len(words[i])):
                if words[i][j] in allowed:
                    count1=count1+1
                else:
                    break
            if count1==len(words[i]):
                count2=count2+1

        return count2
                


        