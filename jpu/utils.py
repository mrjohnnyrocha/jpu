# utils.py
def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:]

def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:]
