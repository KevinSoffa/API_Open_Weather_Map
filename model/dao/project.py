# Project de Retorno da consulta de histórico

PROJECT = {
    '_id': False,
    'id': {'$toString': '$_id'}, # Convertendo para string
    'city': True,
    'lat': True,
    'lon': True,
    'temp': True,
    'date': True
}