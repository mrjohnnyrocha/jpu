# memory.py
class JPUMemory:
    def __init__(self, size):
        self.size = size
        self.memory = [0] * size

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value
