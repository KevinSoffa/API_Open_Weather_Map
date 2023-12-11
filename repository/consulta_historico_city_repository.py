from model.dao.project import PROJECT
from model.dao.mongo import db


def histocorico_city_repository(city: str):
    return db.act_temp.find_one(
        {'city': city},
        PROJECT
    )