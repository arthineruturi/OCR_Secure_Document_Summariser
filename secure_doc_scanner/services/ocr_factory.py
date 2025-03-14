from .ocr_image import ImageOCR
from .ocr_pdf import PDFOCR
from .ocr_base import OCRProcessor

class OCRFactory:
    """Factory for OCR Selection"""
    @staticmethod
    def get_ocr_processor(file_type: str) -> OCRProcessor:
        if file_type in ["jpg", "jpeg", "png"]:
            return ImageOCR()
        elif file_type == "pdf":
            return PDFOCR()
        else:
            raise ValueError("Unsupported file format")
