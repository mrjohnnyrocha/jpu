# api.py
from .core import JPUCore
from .instructions import *
from .memory import JPUMemory

class jpuAPI:
    def __init__(self):
        self.jpu_core = JPUCore()
        self.memory = JPUMemory(1024)  # Example size
        self.jpu_core.connect_memory(self.memory)

    def chdir(self, path):
        instruction = chdir(path)
        self.jpu_core.run([instruction])

    def get_result(self, register):
        return self.jpu_core.registers[register]

    def load_data(self, data, address):
        for i, value in enumerate(data):
            self.memory.write(address + i, value)

    def listdir(self, path='.'):
        instruction = listdir(path)
        return [str(item) for item in self.jpu_core.run([instruction])]

    def mkdir(self, path):
        instruction = mkdir(path)
        self.jpu_core.run([instruction])

    def rm(self, path):
        instruction = rm(path)
        self.jpu_core.run([instruction])

    def run_inference(self, instructions):
        self.jpu_core.run(instructions)

api = jpuAPI()
