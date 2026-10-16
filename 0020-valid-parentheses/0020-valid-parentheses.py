class Solution:
    def isValid(self, s: str) -> bool:
        x=[]
        for ch in s:
            if ch=='(' or ch=='[' or ch=='{':
                x.append(ch)
            else:
                if len(x)==0:
                    return False
                t=x.pop()
                if ch==")" and t=="(":
                    continue
                elif ch=="]" and t=="[":
                    continue
                elif ch=="}" and t=="{":
                    continue
                else:
                    return False
        if len(x)==0:
            return True
        else:
            return False
                    
