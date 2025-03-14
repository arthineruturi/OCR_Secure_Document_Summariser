import logging
from fastapi import APIRouter, UploadFile, File, HTTPException
from services.ocr_factory import OCRFactory
from services.summarization_service import SummarizationService
from storage.local_storage import LocalStorage
import os

router = APIRouter()
ocr_factory = OCRFactory()
summarization_service = SummarizationService()
local_storage = LocalStorage()

logging.basicConfig(level=logging.INFO)
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "pdf", "txt", "docx"}

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Handles file upload, OCR processing, and summarization"""
    file_type = file.filename.split(".")[-1].lower()
    if file_type not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Unsupported file format: {file_type}")

    # Save file locally
    file_path = local_storage.save_file(file)
    logging.info(f"File saved: {file_path}")

    try:
        ocr_processor = ocr_factory.get_ocr_processor(file_type)
        extracted_text = ocr_processor.extract_text(file_path)
        summary = summarization_service.summarize_text(extracted_text) if extracted_text else "No text extracted."

    except ValueError as e:
        logging.error(f"OCR processing error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "filename": file.filename,
        "file_type": file_type,
        "extracted_text": extracted_text[:500] if extracted_text else "No text detected",
        "summary": summary
    }

@router.get("/download/{filename}")
async def download_file(filename: str):
    """Download a stored file"""
    file_path = os.path.join(local_storage.UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        logging.warning(f"File not found: {filename}")
        raise HTTPException(status_code=404, detail="File not found")

    file_data = local_storage.get_file(filename)

    return {"filename": filename, "content": file_data.decode()}

@router.delete("/delete/{filename}")
async def delete_file(filename: str):
    """Delete a stored file"""
    file_path = os.path.join(local_storage.UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        logging.warning(f"Attempted to delete non-existent file: {filename}")
        raise HTTPException(status_code=404, detail="File not found")

    local_storage.delete_file(filename)
    logging.info(f"File deleted: {filename}")

    return {"message": f"{filename} deleted successfully"}
