# jpu/runners/python.py

import runpy
import subprocess
from ..core import JPUCore

class PythonRunner:
    def __init__(self):
        self.jpu_core = JPUCore()

    def execute_code(self, code):
        """Execute the provided Python code sequentially."""
        try:
            exec(code, globals())
        except Exception as e:
            print(f"Error executing Python code: {e}")

    def run_script(self, script_path):
        """Run a Python script located at script_path."""
        try:
            runpy.run_path(script_path)
        except Exception as e:
            print(f"Error running Python script: {e}")
  
    def run_pip_command(self, command, *args):
        """Run a pip command with optional arguments."""
        try:
            full_command = ['pip'] + command + list(args)
            result = subprocess.run(full_command, capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print(result.stderr)
        except Exception as e:
            print(f"Error running pip command: {e}")
