class LocalStorage:
    def upload_file(self, file_name: str, file_data: bytes):
        with open(file_name, "wb") as f:
            f.write(file_data)

    def download_file(self, file_name: str):
        with open(file_name, "rb") as f:
            return f.read()
