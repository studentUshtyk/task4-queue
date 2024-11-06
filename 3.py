from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        return len(self.requests)
recentCounter = RecentCounter()
print(recentCounter.ping(1))       # Запити = [1], повертає 1
print(recentCounter.ping(100))     # Запити = [1, 100], повертає 2
print(recentCounter.ping(3001))    # Запити = [1, 100, 3001], повертає 3
print(recentCounter.ping(3002))    # Запити = [100, 3001, 3002], повертає 3
