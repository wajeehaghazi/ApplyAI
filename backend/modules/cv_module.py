from backend.src.cv_processor import extract_text_from_pdf
from backend.services.openai_service import generate_embedding
from backend.schema.cv_schema import CVUploadResponse
from services.supabase_service import upsert_user

from utils.logger import get_logger
logger= get_logger("cv_module")

def cv_upload(
        user_id: str,
        file_bytes: bytes,
        email: str,

) -> CVUploadResponse:
    logger.info(f"Processing CV upload for user_id: {user_id}, email: {email}")

    extracted_text= extract_text_from_pdf(file_bytes)

    embedding= generate_embedding(extracted_text)

    upsert_user(
        user_id= user_id,
        email= email,
        cv_text= extracted_text,
        cv_embedding= embedding
    )
    
    return CVUploadResponse(
        success= True,
        text_length= len(extracted_text)
    )