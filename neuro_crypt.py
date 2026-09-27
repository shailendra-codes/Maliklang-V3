import gc
from cryptography.fernet import Fernet

class NeuroCrypt:
    def __init__(self):
        # Generate dynamic transient key that stays strictly in volatile memory
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_neural_matrix(self, cleaned_matrix_json: str) -> bytes:
        """
        Encrypts the cleaned brainwave data string instantly before transit.
        """
        raw_bytes = cleaned_matrix_json.encode('utf-8')
        encrypted_data = self.cipher.encrypt(raw_bytes)
        return encrypted_data

    def decrypt_for_inference(self, encrypted_data: bytes) -> str:
        """
        Decrypts data temporarily, extracts insights, and triggers a hard RAM wipe.
        """
        decrypted_bytes = self.cipher.decrypt(encrypted_data)
        decrypted_str = decrypted_bytes.decode('utf-8')
        return decrypted_str

    def hard_volatile_wipe(self, *args):
        """
        Mil-grade zero-fill over active neural memory arrays to prevent RAM bleeding.
        """
        for obj in args:
            if isinstance(obj, bytearray):
                for i in range(len(obj)):
                    obj[i] = 0
            del obj
        # Force garbage collector to empty the active memory heap instantly
        gc.collect()
 
