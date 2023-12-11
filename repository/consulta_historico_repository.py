from model.dao.project import PROJECT
from model.dao.mongo import db


def consulta_historico_repository():
    
    # Faz chamada GET ALL no Banco de Dados 
    response = db.act_temp.find(
        {},
        PROJECT
    )

    return {'historico': list(response)}
