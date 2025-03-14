import os
from fastapi import UploadFile

class LocalStorage:
    """Handles local file storage"""
    
    UPLOAD_DIR = "uploads/"

    def __init__(self):
        os.makedirs(self.UPLOAD_DIR, exist_ok=True)  # Ensure uploads folder exists

    def save_file(self, file: UploadFile) -> str:
        """Saves uploaded file locally"""
        file_path = os.path.join(self.UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return file_path

    def get_file(self, file_name: str) -> bytes:
        """Retrieves file content"""
        file_path = os.path.join(self.UPLOAD_DIR, file_name)
        with open(file_path, "rb") as f:
            return f.read()

    def delete_file(self, file_name: str):
        """Deletes a file"""
        file_path = os.path.join(self.UPLOAD_DIR, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)


