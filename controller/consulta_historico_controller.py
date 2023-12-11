from service import consulta_historico_service
from fastapi import status
from .router import router


@router.get('/historico', status_code=status.HTTP_200_OK)

# Define rota para chamar a função GET no Banco de Dados
def consulta_historico_controller():

    return consulta_historico_service()
