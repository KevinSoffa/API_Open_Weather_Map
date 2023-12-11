from repository import get_repository
from fastapi import HTTPException
from datetime import datetime
from model.dao.mongo import db


def get_service(dto:dict):
    '''
        Tratamento de dados para retornar no Controller
        e Captura de dados para salvar Histórico de pesquisas
        no Mongo DB
    '''

    response = get_repository(dto)

    if response:
        
        city_name = response['city']['name']
        lat = response['city']['coord']['lat']
        lon = response['city']['coord']['lon']
        temp = response['list'][0]['main']['temp']
        data_atual = datetime.now()
        print(temp)


        historico = {
            'city': city_name,
            'lat': lat,
            'lon': lon,
            'temp': temp,
            'date': data_atual
        }

        # Histórico no banco de dados
        result = db.act_temp.insert_one(historico)

        if result.inserted_id:
            print(f'Histórico salvo com Sucesso!. ID: {result.inserted_id}')
        
        else:
            print('Falha ao Salvar o Histórico')

        return response
    
    raise HTTPException(status_code=404)
