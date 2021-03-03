from init_database_reddit import __create_connection
from os.path import join
from utils.dict_factory import _dict_factory
from utils.config import DATABASE_PATH

CURRENT_CURSOR = None


def update_current_database(database_name: str):
    CURRENT_CONNECTION = __create_connection(
        join(DATABASE_PATH, f"{database_name}.db"))
    CURRENT_DATABASE_NAME = database_name
    print(f"CONNECTION : {CURRENT_CONNECTION}")
    print(f"CURRENT_DATABASE_NAME : {CURRENT_DATABASE_NAME}")
    CURRENT_CONNECTION.row_factory = _dict_factory
    CURRENT_CURSOR = CURRENT_CONNECTION.cursor()
    print(f"CURSOR : {CURRENT_CURSOR}")
    return CURRENT_CURSOR
