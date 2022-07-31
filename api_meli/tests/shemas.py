from pydantic import BaseModel


class ListFilesResponse(BaseModel):
    id: str
    name: str


class CreateFileResponse(BaseModel):
    id: str
    titulo: str
    descripcion: str
