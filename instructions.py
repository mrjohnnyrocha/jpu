# instructions.py
def load(reg, addr):
    return {'op': 'LOAD', 'reg': reg, 'addr': addr}

def store(addr, reg):
    return {'op': 'STORE', 'addr': addr, 'reg': reg}

def add(reg, reg1, reg2):
    return {'op': 'ADD', 'reg': reg, 'reg1': reg1, 'reg2': reg2}

# Add more instructions as needed
