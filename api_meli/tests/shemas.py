from pydantic import BaseModel
from typing import List, Optional

class ListFilesResponse(BaseModel):
    id: str
    name: str

class CreateFileResponse(BaseModel):
    id: str
    titulo: str
    descripcion: str