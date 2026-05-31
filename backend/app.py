from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Depends,
    Request)

from fastapi.responses import (
    JSONResponse,
    StreamingResponse)

from backend.src.cv_processor import (
    extract_text_from_pdf)

from backend.src.jwt_auth import (
    get_current_user)

from backend.src.sse_manager import (
    pipeline_event_stream)

from backend.schema.cv_schema import (
    CVUploadResponse
)

from backend.schema.pipeline_schema import (
    PipelineRunResponse)

from backend.modules.pipeline_module import (
    trigger_pipeline)

from backend.utils.logger import (
    get_logger)

from backend.utils.custom_exceptions import (
    InvalidFileError,
    AuthenticationError,
    NotFoundError,
    PipelineError
)


app = FastAPI()

logger = get_logger("app")

@app.exception_handler(InvalidFileError)
async def invalid_file_handler(
    request: Request,
    exc: InvalidFileError):

    return JSONResponse(
        status_code=400,
        content={
            "error": str(exc)
        }
    )


@app.exception_handler(AuthenticationError)
async def authentication_handler(
    request: Request,
    exc: AuthenticationError):

    return JSONResponse(
        status_code=401,
        content={
            "error": str(exc)
        }
    )

@app.exception_handler(NotFoundError)
async def not_found_handler(
    request: Request,
    exc: NotFoundError):

    return JSONResponse(
        status_code=404,
        content={
            "error": str(exc)
        }
    )


@app.exception_handler(PipelineError)
async def pipeline_handler(
    request: Request,
    exc: PipelineError):

    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc)
        }
    )

@app.get("/api/health")
def health_check():

    logger.info("Health endpoint called")

    return {
        "status": "ok"
    }

@app.post(
    "/api/cv/upload",
    response_model=CVUploadResponse
)
async def upload_cv(
    file: UploadFile = File(...)
):

    logger.info(
        f"Processing file: {file.filename}"
    )

    file_bytes = await file.read()

    text = extract_text_from_pdf(
        file_bytes
    )

    return CVUploadResponse(
        success=True,
        text_length=len(text)
    )

@app.post(
    "/api/pipeline/run",
    response_model=PipelineRunResponse
)
def run_pipeline(
    user_id: str = Depends(
        get_current_user
    )
):

    logger.info(
        f"Pipeline requested by {user_id}"
    )

    return trigger_pipeline(
        user_id
    )


@app.get(
    "/api/pipeline/{run_id}/stream"
)
async def stream_pipeline(
    run_id: str
):

    return StreamingResponse(
        pipeline_event_stream(
            run_id
        ),
        media_type="text/event-stream"
    )


@app.get("/api/jobs/{run_id}")
def get_jobs(
    run_id: str
):
    return {
        "message": "Jobs endpoint coming soon",
        "run_id": run_id
    }


@app.get("/api/job/{job_match_id}")
def get_job(
    job_match_id: str
):
    return {
        "message": "Job detail endpoint coming soon",
        "job_match_id": job_match_id
    }


@app.post("/api/email-draft/{job_match_id}")
def regenerate_email(
    job_match_id: str
):
    return {
        "message": "Email generation endpoint coming soon",
        "job_match_id": job_match_id
    }


@app.patch("/api/jobs/{job_match_id}")
def update_job_status(
    job_match_id: str
):
    return {
        "message": "Status update endpoint coming soon",
        "job_match_id": job_match_id
    }


@app.get("/api/applications")
def get_applications():
    return {
        "message": "Applications endpoint coming soon"
    }


@app.get("/")
def root():
    return {
        "message": "ApplyAI API running"
    }