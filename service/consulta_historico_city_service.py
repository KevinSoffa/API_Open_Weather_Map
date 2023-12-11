from repository import histocorico_city_repository
from fastapi import HTTPException


def consulta_historico_city_service(city: str):
    response = histocorico_city_repository(city)

    if response:
        return response
    
    raise HTTPException(400, 'Registro não encontrado')
