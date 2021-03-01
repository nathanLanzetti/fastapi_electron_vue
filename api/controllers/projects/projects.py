import sqlite3
import os
from os.path import join
from init_database_reddit import __create_connection
from utils.dict_factory import _dict_factory
from models.monsterhunter.monsters import BaseMonster
from utils.databases_connections import cursor_monsterhunter as c
from utils import current_database


def open_projects(database_name: str):
    current_database.update_current_database(database_name)
    return database_name
