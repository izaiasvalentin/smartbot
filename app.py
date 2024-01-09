from flask import Flask
from flask_cors import CORS, cross_origin
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

app = Flask(__name__)
CORS(app)

@app.get('/')
def index():
    return 'smartapi'

@app.get('/<palavra>')
def cripto_mensagem(palavra):
    chave = b'c21hcnRib3Q2@g5f'
    iv = b'RP2otAWFtvZY0gT1'
    cipher = Cipher(algorithms.AES(chave), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    mensagem_cifrada = encryptor.update(palavra.encode()) + encryptor.finalize()
    return base64.b64encode(mensagem_cifrada).decode()   

if __name__ == '__main__':
    app.run()