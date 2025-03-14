class OCRProcessor:
    """Base class for OCR processing"""
    def extract_text(self, file_path: str) -> str:
        raise NotImplementedError
