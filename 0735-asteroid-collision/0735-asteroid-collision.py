class Solution(object):
    def asteroidCollision(self, asteroids):
        x=[]
        for i in range(len(asteroids)):
            if(asteroids[i]>0 and len(x)>0 and x[-1]<0) or (asteroids[i]<0 and len(x)>0 and x[-1]>0):
                j=-1
                while len(x)>0:
                    if x[j]<0:
                        x.append(asteroids[i])
                        break
                    if abs(x[j])==abs(asteroids[i]):
                        x.pop()
                        break
                    if abs(x[j])>abs(asteroids[i]):
                        break
                    else:
                        x.pop()
                        if len(x)==0:
                            x.append(asteroids[i])
                            break
            elif asteroids[i]>0:
                x.append(asteroids[i])
            elif (asteroids[i]<0 and len(x)==0) or (asteroids[i]<0 and x[-1]<0):
                x.append(asteroids[i])
        return(x)

        