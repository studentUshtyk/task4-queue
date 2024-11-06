class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k  
        self.front = -1 
        self.rear = -1   
        self.size = 0  

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0  
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value  
        self.size += 1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity  
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1  
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
myCircularQueue = MyCircularQueue(3)

print(myCircularQueue.enQueue(1))  # True
print(myCircularQueue.enQueue(2))  # True
print(myCircularQueue.enQueue(3))  # True
print(myCircularQueue.enQueue(4))  # False, черга заповнена

print(myCircularQueue.Rear())  # 3

print(myCircularQueue.isFull())  # True

print(myCircularQueue.deQueue())  # True

print(myCircularQueue.enQueue(4))  # True

print(myCircularQueue.Rear())  # 4
