import sqlite3
import os
from os.path import join
from init_database_reddit import __create_connection
from utils.dict_factory import _dict_factory
from models.monsterhunter.monsters import BaseMonster
from utils.databases_connections import cursor_monsterhunter as c


def get_monsters():
    statement = ''' SELECT * FROM monsters'''
    c.execute(statement)
    return c.fetchall()


def get_monster_by_id(monster_id: int):
    statement = ''' SELECT * from monsters where monster_id=?'''
    c.execute(statement, (monster_id, ))
    return c.fetchone()


def create_monster(monster_to_create: dict):
    # print(tuple(monster_to_create.values()))
    statement = ''' INSERT INTO monsters(name, description, hp)
                    VALUES (?,?,?)'''
    c.execute(statement, tuple(monster_to_create.values()))
    c.commit()
    return c.lastrowid
