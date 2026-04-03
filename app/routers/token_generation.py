from app.core import task_logger
from app.helpers import helper
from fastapi import APIRouter
from app.schemas.token_generation import TokenGenerationRequest, TokenGenerationResponse

api_router = APIRouter()

@api_router.post("/v1/generate-token", tags=["Token Generation"], response_model=TokenGenerationResponse)
def generate_token(user_data: TokenGenerationRequest):
    try:
        user_name = user_data.username
        generated_token = helper.generate_access_token(user_name)
        return TokenGenerationResponse(access_token=generated_token)
    except Exception as e:
        task_logger.exception(e)

