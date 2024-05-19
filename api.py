# api.py
from .core import JPUCore
from .memory import JPUMemory

class jpuAPI:
    def __init__(self):
        self.jpu_core = JPUCore()
        self.memory = JPUMemory(1024)  # Example size
        self.jpu_core.connect_memory(self.memory)

    def load_data(self, data, address):
        for i, value in enumerate(data):
            self.memory.write(address + i, value)

    def run_inference(self, instructions):
        self.jpu_core.run(instructions)

    def get_result(self, register):
        return self.jpu_core.registers[register]

api = jpuAPI()
print(api.__dict__)
print(api.load_data([1, 2, 3], 10))
print(api.run_inference([{'op':'LOAD', 'reg':0, 'addr':10}, {'op':'LOAD', 'reg':1, 'addr':11}, {'op':'ADD', 'reg':2, 'reg1':0, 'reg2':1}]))
print(api.get_result(2))