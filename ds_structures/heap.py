import heapq

class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, x):
        heapq.heappush(self.data, x)

    def pop(self):
        return heapq.heappop(self.data)

    def peek(self):
        return self.data[0]

    def visualize(self):
        print("Heap:", self.data)