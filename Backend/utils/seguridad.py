# Backend/utils/seguridad.py

import hashlib
import os

def hash_to_brainfuck(password: str) -> str:
    salt = os.urandom(16)
    hashed = hashlib.sha256(salt + password.encode()).hexdigest()
    salted_hash = salt.hex() + hashed
    return to_brainfuck(salted_hash)

def to_brainfuck(text: str) -> str:
    result = ''
    prev = 0
    for char in text:
        diff = ord(char) - prev
        if diff > 0:
            result += '+' * diff
        elif diff < 0:
            result += '-' * (-diff)
        result += '.'
        prev = ord(char)
    return result
