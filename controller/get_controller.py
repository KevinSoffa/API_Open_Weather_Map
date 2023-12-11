from fastapi import status, Depends
from model.dto import ListagemDTO
from service import get_service
from .router import router


@router.get('', status_code=status.HTTP_200_OK)
def get_controller(
    listagem_dto: ListagemDTO = Depends()
):
    return get_service(listagem_dto.__dict__,)
