from app.schemas import SchemaBaseModel

class TokenGenerationRequest(SchemaBaseModel):
    username: str

class TokenGenerationResponse(SchemaBaseModel):
    access_token: str