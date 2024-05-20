# core.py
import os

class JPUCore:
    def __init__(self):
        self.registers = [0] * 32  # Simplified register set
        self.memory = None

    def connect_memory(self, memory):
        self.memory = memory

    def execute(self, instruction):
        if instruction['op'] == 'ADD':
            self.registers[instruction['reg']] = self.registers[instruction['reg1']] + self.registers[instruction['reg2']]
        elif instruction['op'] == 'CHDIR':
            os.chdir(instruction['path'])
        elif instruction['op'] == 'LOAD':
            self.registers[instruction['reg']] = self.memory.read(instruction['addr'])
        elif instruction['op'] == 'LISTDIR':
            return os.listdir(instruction['path'])
        elif instruction['op'] == 'MKDIR':
            os.makedirs(instruction['path'], exist_ok=True)
        elif instruction['op'] == 'RM':
            if os.path.isdir(instruction['path']):
                os.rmdir(instruction['path'])
            else:
                os.remove(instruction['path'])
        elif instruction['op'] == 'STORE':
            self.memory.write(instruction['addr'], self.registers[instruction['reg']])
        # Add more instructions as needed

    def run(self, instructions):
        results = []
        for instruction in instructions:
            result = self.execute(instruction)
            if result is not None:
                results.append(result)
        return results
