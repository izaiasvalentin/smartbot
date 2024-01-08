from fastapi import FastAPI
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64


app = FastAPI()

@app.get("/{mensagem}")
def cripto_mensagem(mensagem: str):
    chave = b'c21hcnRib3Q2@g5f'
    iv = b'RP2otAWFtvZY0gT1'
    cipher = Cipher(algorithms.AES(chave), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    mensagem_cifrada = encryptor.update(mensagem.encode()) + encryptor.finalize()
    return base64.b64encode(mensagem_cifrada).decode()    