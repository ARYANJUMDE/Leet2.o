import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        states = (minutesToTest // minutesToDie) + 1
        return int(math.ceil(math.log(buckets) / math.log(states) - 1e-10))