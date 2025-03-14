import pytesseract
from pdf2image import convert_from_path
from .ocr_base import OCRProcessor  # Import base class

class PDFOCR(OCRProcessor):
    """Extracts text from PDF files"""
    def extract_text(self, file_path: str) -> str:
        images = convert_from_path(file_path)
        return " ".join([pytesseract.image_to_string(img) for img in images])
