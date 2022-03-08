class Q:
    def __init__(self, size):
        self.size = size
        self.q = [None for _ in range(self.size)]
        self.enq = -1
        self.dq = -1
        print("Q created")
    
    def enque(self, a):
        if self.enq == -1:
            self.enq = 0
            self.dq = 0
            self.q[self.enq] = a
        elif (self.enq+1)%self.size == self.dq:
            print("q is full")
        else:
            self.enq = (self.enq+1) % self.size
            self.q[self.enq] = a
        
    def deq(self):
        if self.enq == -1:
            print("Q empty")
        elif self.enq == self.dq:
            result = self.q[self.dq]
            self.enq, self.deq = -1, -1
            return result
        else:
            result = self.q[self.dq]
            self.dq = (self.dq+1) % self.size
            return result
            
        
    def peek(self):
        a= self.q[self.dq]
        print("peek is ", a)
        return a
    
    def print(self):
        print(self.q)
    
q = Q(5)
q.enque(2)
q.enque(8)
q.enque(4)
q.enque(1)
q.enque(6)
q.deq()
q.print()
q.enque(89)
q.print()
