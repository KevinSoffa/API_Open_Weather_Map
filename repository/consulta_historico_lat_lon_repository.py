from model.dao.project import PROJECT
from model.dao.mongo import db


def consulta_historico_lat_lon_repository(lat: str, lon: str):
    return db.act_temp.find_one(
        {'lat': float(lat), 'lon': float(lon)},
        PROJECT
    )
