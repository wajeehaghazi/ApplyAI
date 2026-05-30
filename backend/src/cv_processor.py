from io import BytesIO
from PyPDF2 import PdfReader
from backend.utils.custom_exceptions import InvalidFileError

MAX_FILE_SIZE = 5 * 1024 * 1024

def extract_text_from_pdf(file_bytes: bytes) -> str:
    if len(file_bytes) > MAX_FILE_SIZE:
        raise InvalidFileError("File size exceeds the maximum allowed size 5MB")
    try:
        pdf_reader= PdfReader(BytesIO(file_bytes))
         
        extracted_text= ""
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

    except Exception:
        raise InvalidFileError("Failed to process the PDF file. Ensure it's a valid PDF.")
    
    if not extracted_text.strip():
        raise InvalidFileError("PDF contains no readable text.")
    
    return extracted_text