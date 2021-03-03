from utils import current_database


def open_projects(database_name: str):
    current_database.update_current_database(database_name)
    return database_name
