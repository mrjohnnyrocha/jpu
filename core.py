# core.py
class JPUCore:
    def __init__(self):
        self.registers = [0] * 32  # Simplified register set
        self.memory = None

    def connect_memory(self, memory):
        self.memory = memory

    def execute(self, instruction):
        # Simplified execution of instructions
        if instruction['op'] == 'LOAD':
            self.registers[instruction['reg']] = self.memory.read(instruction['addr'])
        elif instruction['op'] == 'STORE':
            self.memory.write(instruction['addr'], self.registers[instruction['reg']])
        elif instruction['op'] == 'ADD':
            self.registers[instruction['reg']] = self.registers[instruction['reg1']] + self.registers[instruction['reg2']]
        # Add more instructions as needed

    def run(self, instructions):
        for instruction in instructions:
            self.execute(instruction)
