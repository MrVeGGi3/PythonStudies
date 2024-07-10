from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroAtleta

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example='25')]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta em KG', example='50.5')]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta em Metros', example='1.80')]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Nome da Categoria', example='Scale', max_length=30)]
    centro_treinamento: Annotated[CentroAtleta, Field(description='Nome do Centro de Treinamento', example='CT', max_length=30)]
class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do Atleta', example='João', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do Atleta', example='25')]