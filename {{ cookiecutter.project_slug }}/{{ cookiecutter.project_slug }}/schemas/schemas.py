from pydantic import BaseModel

class Message(BaseModel):
    """Details for errors or health checks"""
    detail: str
