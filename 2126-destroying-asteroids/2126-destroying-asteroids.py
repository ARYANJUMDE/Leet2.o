class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        t=max(asteroids)
        for i in range(len(asteroids)):
            if mass>=asteroids[i]:
                mass=mass+asteroids[i]
            elif mass>=t:
                return True
            else:
                return False
        return True
        