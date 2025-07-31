import hashlib

# Utiliza un identificador como sal (email por ejemplo)
def hash_to_brainfuck(password: str, salt: str) -> str:
    # Hasheo seguro con salt fijo (email u otro campo único)
    salted = (salt + password).encode()
    hashed = hashlib.sha256(salted).hexdigest()  # 64 chars hex
    return to_brainfuck(hashed)


def to_brainfuck(text: str) -> str:
    # Convertimos de forma determinista cada carácter
    return ''.join('+' * ord(c) + '.' for c in text)
