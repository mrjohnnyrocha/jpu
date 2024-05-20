# test_core.py
import unittest
from core import JPUCore
from memory import JPUMemory
from instructions import load, store, add

class TestJPUCore(unittest.TestCase):
    def test_execution(self):
        core = JPUCore()
        memory = JPUMemory(1024)
        core.connect_memory(memory)

        instructions = [
            load(0, 10),  # Load from address 10 to register 0
            load(1, 20),  # Load from address 20 to register 1
            add(2, 0, 1)  # Add registers 0 and 1, store in register 2
        ]

        memory.write(10, 5)
        memory.write(20, 10)
        core.run(instructions)
        self.assertEqual(core.registers[2], 15)

if __name__ == '__main__':
    unittest.main()
