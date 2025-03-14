import os
from fastapi import UploadFile

class FileHandler:
    """Handles File Operations for Local Storage"""

    def __init__(self, storage_path="uploads/"):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True) 

    def save_file(self, file: UploadFile) -> str:
        """Saves uploaded file locally"""
        file_path = os.path.join(self.storage_path, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return file_path

    def load_file(self, filename: str) -> bytes:
        """Loads file content"""
        file_path = os.path.join(self.storage_path, filename)
        with open(file_path, "rb") as f:
            return f.read()

    def delete_file(self, filename: str):
        """Deletes a file"""
        file_path = os.path.join(self.storage_path, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
