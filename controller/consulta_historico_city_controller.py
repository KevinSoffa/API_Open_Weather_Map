from service import consulta_historico_city_service
from fastapi import status
from .router import router


# Pesquisa por nome de Cidade
@router.get('/historico/city/{city}', status_code=status.HTTP_200_OK)
def consulta_historico_city_controller(city: str):
    return consulta_historico_city_service(city)
