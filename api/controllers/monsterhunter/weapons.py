import sqlite3
import os
from os.path import join
from init_database_reddit import __create_connection
from utils.dict_factory import _dict_factory
from utils.databases_connections import cursor_monsterhunter as c


def get_weapons():
    statement = ''' SELECT * FROM weapons'''
    c.execute(statement)
    return c.fetchall()


def get_weapons_by_id(weapon_id: int):
    statement = ''' SELECT * from weapons where weapons_id=?'''
    c.execute(statement, (weapon_id, ))
    return c.fetchone()
