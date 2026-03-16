class MyCircularDeque(object):

    def __init__(self, k):
        self.k = k
        self.q = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        
        self.front = (self.front - 1) % self.k
        self.q[self.front] = value
        self.count += 1
        
        if self.count == 1:
            self.rear = self.front
            
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        self.count += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        
        self.rear = (self.rear - 1) % self.k
        self.count -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()