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
    pass
