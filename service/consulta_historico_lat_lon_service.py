from repository import consulta_historico_lat_lon_repository
from fastapi import HTTPException


def consulta_historico_lat_lon_service(lat: str, lon: str):
    response = consulta_historico_lat_lon_repository(lat, lon)

    if response:
        return response
    
    raise HTTPException(400, 'Registro não encontrado')