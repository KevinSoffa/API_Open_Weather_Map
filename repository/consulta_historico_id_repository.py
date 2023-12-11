from model.dao.project import PROJECT
from model.dao.mongo import db
from datetime import datetime
from bson import ObjectId


def consulta_historico_id_repository(id: str):
    
    query = {}
    # Pesquisa por esse parametros
    if id:
        query['_id'] = ObjectId(id)

    return db.act_temp.find_one(query, PROJECT)