# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:22:39+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class PngPostRequest(BaseModel):
    file: bytes = Field(..., description='File to handle')
