import sqlite3
import os
from os.path import join
from utils.dict_factory import _dict_factory
from init_database_reddit import __create_connection
from utils.config import DATABASE_PATH

print(DATABASE_PATH)
conn_monsterhunter = __create_connection(
    join(DATABASE_PATH, "monsterhunter.db"))
conn_monsterhunter.row_factory = _dict_factory
cursor_monsterhunter = conn_monsterhunter.cursor()


conn_reddit = __create_connection(join(DATABASE_PATH, "reddit.db"))
conn_reddit.row_factory = _dict_factory
cursor_reddit = conn_reddit.cursor()
