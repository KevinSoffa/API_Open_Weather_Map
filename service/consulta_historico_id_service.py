from repository import consulta_historico_id_repository
from fastapi import HTTPException
from bson import ObjectId


def consulta_historico_id_service(id: ObjectId):
    
    response = consulta_historico_id_repository(str(id))

    if response:
        return response
    
    raise HTTPException(400, "Registro não encontrado")