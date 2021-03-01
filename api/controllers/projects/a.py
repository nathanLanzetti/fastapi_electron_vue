import sqlite3
import os
from os.path import join
from init_database_reddit import __create_connection
from utils.dict_factory import _dict_factory
from models.monsterhunter.monsters import BaseMonster
from utils.current_database import CURRENT_CURSOR as c


def get_project_name():

    statement = ''' SELECT * FROM a WHERE project_id=1'''
    print(globals())
    # c.execute(statement)
    # print(c.fetchone())
    # return c.fetchone()
    return "hello"
