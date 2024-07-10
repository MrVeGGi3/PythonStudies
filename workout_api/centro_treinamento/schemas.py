from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema

class CentroIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT', max_length=20)]
    endereco: Annotated[str, Field(description='Endreço do Centro de Treinamento', example='Avenida das Jabuticabeiras', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do Centro de Treinamento', example='CT', max_length=30)]

class CentroAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT', max_length=20)]

class CentroOut(CentroAtleta):
    id: Annotated[UUID4, Field(description='Identificador do Centro de Treinamento')]