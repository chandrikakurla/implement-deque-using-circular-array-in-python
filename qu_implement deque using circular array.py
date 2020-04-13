#class to implement deque 
class Deque:
    def __init__(self,size):
        #initialising deque to given size
        self.deque=[None] *size
        self.size=size
        self.front=-1
        self.rear=-1
    def isFull(self):
        if((self.front==0 and self.rear==self.size-1) or (self.front==self.rear+1)):
            return True
        else:
            return False
    def isEmpty(self):
        if self.front==-1:
            return True
        else:
            return False
    def insert_front(self,data):
        if self.isFull():
            print("deque is full")
            return
        elif self.isEmpty():
            self.front=0
            self.rear=0
        elif self.front==0:
            self.front=self.size-1
        else:
            self.front=self.front-1
        self.deque[self.front]=data
    def insert_rear(self,data):
        if self.isFull():
            print("deque is full")
            return
        elif self.isEmpty():
            self.front=0
            self.rear=0
        elif self.rear==self.size-1:
            self.rear=0
        else:
            self.rear+=1
        self.deque[self.rear]=data
    def Delete_front(self):
        if self.isEmpty():
            print("deque is empty")
            return
        elif(self.front==self.rear):
            self.front=-1
            self.rear=-1
        elif(self.front==self.size-1):
            self.front=0
        else:
            self.front=self.front+1
    def Delete_rear(self):
        if self.isEmpty():
            print("deque is empty")
            return
        elif self.front==self.rear:
            self.front=-1
            self.rear=-1
        elif self.rear==0:
            self.rear=self.size-1
        else:
            self.rear=self.rear-1
    def get_Front(self):
        if self.isEmpty():
            print("deque is empty")
            return
        else:
            return self.deque[self.front]
    def get_Rear(self):
        if self.isEmpty():
            print("deque is empty")
            return
        else:
            return self.deque[self.rear]
if __name__=="__main__":
    deq=Deque(6)
    deq.insert_rear(1)
    deq.insert_rear(2)
    deq.insert_front(3)
    deq.insert_front(4)
    deq.insert_rear(5)
    deq.insert_front(6)
    #deq.Delete_rear()
    #deq.Delete_front()
    print(deq.get_Front())
    print(deq.get_Rear())
    

    
        
        
