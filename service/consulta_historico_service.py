from repository import consulta_historico_repository
from fastapi import HTTPException


def consulta_historico_service():

    # Mostra os dados e retorna erro se tiver
    response = consulta_historico_repository()

    if response:
        return response or []
    
    raise HTTPException(400)
