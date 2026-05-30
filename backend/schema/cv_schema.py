from pydantic import BaseModel

class CVUploadResponse(BaseModel):
    success: bool
    text_length: int