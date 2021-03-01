from init_database_reddit import __create_connection
from os.path import join
import os
import sqlite3
from utils.dict_factory import _dict_factory
from utils.databases_connections import cursor_reddit as c


def get_users():
    statement: str = ''' SELECT * FROM users '''
    c.execute(statement)
    results = c.fetchall()
    return results


def get_user_by_id(id: int):
    statement: str = ''' SELECT * FROM users WHERE user_id=?'''
    c.execute(statement, (id, ))
    return c.fetchone()


def get_user_with_comments(id: int):
    # conn.row_factory = sqlite3.Row
    # cursor = conn.cursor()
    # statementUser: str = ''' SELECT * FROM users WHERE user_id=?'''
    # statementComments: str = ''' SELECT * FROM posts WHERE user_id=?'''
    # cursor.execute(statement, (id, ))
    # return cursor.fetchall()[0]
    pass
