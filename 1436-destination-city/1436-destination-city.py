class Solution(object):
    def destCity(self, paths):
        x=set()
        for i in range(len(paths)):
            if paths[i][1] not in x:
                x.add(paths[i][1])
        for i in range(len(paths)):
            if paths[i][0] in x:
                x.remove(paths[i][0])
        x=list(x)
        return x[0]
