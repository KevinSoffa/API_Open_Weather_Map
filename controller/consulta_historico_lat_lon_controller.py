from service import consulta_historico_lat_lon_service
from fastapi import status
from .router import router


# Pesquisa por latitude e longitode
@router.get('/historico/lat/{lat}/lon/{lon}', status_code=status.HTTP_200_OK)
def consulta_historico_lat_lon_controller(lat: str, lon: str):
    return consulta_historico_lat_lon_service(lat, lon)
