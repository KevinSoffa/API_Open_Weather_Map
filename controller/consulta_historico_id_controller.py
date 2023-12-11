from service import consulta_historico_id_service
from fastapi import status, HTTPException
from datetime import datetime
from bson import ObjectId
from .router import router


# Definindo end ponts para pesquisa
#Pesquisa por ID
@router.get('/historico/{id}', status_code=status.HTTP_200_OK)


def consulta_historico_id_controller(id: str):
    return consulta_historico_id_service(id)