from datetime import datetime
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.atleta.models import AtletaModel
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentrotreinamentoModel
from uuid import uuid4
from sqlalchemy.future import select
router = APIRouter()
@router.post(
    '/',
    summary='Criar um novo Atleta',
    status_code= status.HTTP201_CREATED,
    response_model=AtletaOut

)
async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    categoria_name = atleta_in.categoria.nome
    centro_name = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_name))
    ).scallars().first()


    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'A Categoria{categoria_name} não foi encontrada.'
        )

    centro_de_treinamento = (await db_session.execute(
        select(CentrotreinamentoModel).filter_by(nome=centro_name))
    ).scallars().first()


    if not centro_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'O Centro de Treinamento{centro_name} não foi encontrada.'
        )
    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.now(datetime.UTC),**atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_de_treinamento'}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_de_treinamento_id = centro_de_treinamento.pk_id
        db_session.add(atleta_model)
        await db_session.commit() 
    except Exception:
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Ocorreu um erro ao inserir os dados no banco'


    return atleta_out



@router.get(
        '/',
        summary='Consultar todos os Atletas',
        status_code= status.HTTP_200_OK,
        response_model=list[AtletaOut]
)
async def query(db_session: DatabaseDependency)-> list[AtletaOut]:
    atletas : list[AtletaOut] = (await db_session.execute(select(AtletaModel))).scallars().all()

    return[AtletaOut.model_validate(atleta) for atleta in atletas]

@router.get(
        '/{id}',
        summary='Consultar um atleta pelo id',
        status_code= status.HTTP_200_OK,
        response_model=AtletaOut,
)
async def query(id : UUID4, db_session: DatabaseDependency)-> AtletaOut:
    atleta : AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scallars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail = f'Categoria não encontrada do ID {id}'
        )
    return atleta

@router.patch(
        '/{id}',
        summary='Editar um atleta pelo id',
        status_code= status.HTTP_200_OK,
        response_model=AtletaOut,
)
async def query(id : UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...))-> AtletaOut:
    atleta : AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scallars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail = f'Categoria não encontrada do ID {id}'
        )
    
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.itens():
        setattr(atleta, key, value)
    
    await db_session.commit()
    await db_session.refresh(atleta)
    return atleta

@router.delete(
    '/{id}',
    summary='Consultar um atleta pelo id',
    status_code= status.HTTP_204_NO_CONTENT
)
async def query(id : UUID4, db_session: DatabaseDependency)-> None:
    atleta : AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
        ).scallars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail = f'Categoria não encontrada do ID {id}'
        )
    
    await db_session.delete(atleta)
    await db_session.commit()
    