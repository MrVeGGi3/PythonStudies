from fastapi import APIRouter, HTTPException, status, Body
from uuid import uuid4
from pydantic import UUID4
from sqlalchemy.future import select
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.centro_treinamento.schemas import CentroIn, CentroOut
from workout_api.centro_treinamento.models import CentrotreinamentoModel
router = APIRouter()
@router.post(
        '/',
        summary='Criar um novo centro de Treinamento',
        status_code= status.HTTP201_CREATED,
        response_model=CentroOut,
)
async def post(
    db_session: DatabaseDependency, 
    centro_in: CentroIn = Body(...)
)-> CentroOut:
    centro_out = CentroOut(id=uuid4(), **centro_in.model_dump())
    centro_model = CentrotreinamentoModel(**centro_out.model_dump())

    db_session.add(centro_model)
    await db_session.commit()
    return centro_out

@router.get(
        '/',
        summary='Consultar todos os Centros de Treinamento',
        status_code= status.HTTP_200_OK,
        response_model=list[CentroOut]
)
async def query(db_session: DatabaseDependency)-> list[CentroOut]:
    centros : list[CentroOut] = (await db_session.execute(select(CentrotreinamentoModel))).scallars().all()
    return centros

@router.get(
        '/{id}',
        summary='Consultar um Centro de Treinamento pelo id',
        status_code= status.HTTP_200_OK,
        response_model=CentroOut
)
async def query(id : UUID4, db_session: DatabaseDependency)-> CentroOut:
    centro_out : CentroOut = (
        await db_session.execute(select(CentrotreinamentoModel).filter_by(id=id))
        ).scallars().first()
    
    if not centro_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail = f'Centro de Treinamento não encontrado no ID {id}'
        )
    return centro_out