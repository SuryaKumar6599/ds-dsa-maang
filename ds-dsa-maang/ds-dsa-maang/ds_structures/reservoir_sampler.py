import random

class ReservoirSampler:
    def __init__(self):
        self.count = 0
        self.sample = None

    def add(self, x):
        self.count += 1
        if random.randint(1, self.count) == 1:
            self.sample = x
        print("Current sample:", self.sample)