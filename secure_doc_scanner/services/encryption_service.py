from cryptography.fernet import Fernet

class EncryptionService:
    """AES-256 Encryption"""
    
    def __init__(self, key: bytes = None):
        self.key = key or Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_text(self, plain_text: str) -> bytes:
        return self.cipher_suite.encrypt(plain_text.encode())

    def decrypt_text(self, encrypted_text: bytes) -> str:
        return self.cipher_suite.decrypt(encrypted_text).decode()
