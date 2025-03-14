import pytesseract
from PIL import Image
from .ocr_base import OCRProcessor  # Import base class

class ImageOCR(OCRProcessor):
    """Extracts text from image files"""
    def extract_text(self, file_path: str) -> str:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)
