# instructions.py
def add(reg, reg1, reg2):
    return {'op': 'ADD', 'reg': reg, 'reg1': reg1, 'reg2': reg2}

def chdir(path):
    return {'op': 'CHDIR', 'path': path}

def listdir(path='.'):
    return {'op': 'LISTDIR', 'path': path}

def load(reg, addr):
    return {'op': 'LOAD', 'reg': reg, 'addr': addr}

def mkdir(path):
    return {'op': 'MKDIR', 'path': path}

def rm(path):
    return {'op': 'RM', 'path': path}

def store(addr, reg):
    return {'op': 'STORE', 'addr': addr, 'reg': reg}

# Add more instructions as needed
