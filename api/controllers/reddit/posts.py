from utils.databases_connections import cursor_reddit as c


def get_posts():
    statement: str = ''' SELECT * FROM posts '''
    c.execute(statement)
    results = c.fetchall()
    return results


def get_post_by_id(id: int):
    statement: str = ''' SELECT * FROM posts WHERE post_id=?'''
    c.execute(statement, (id, ))
    return c.fetchall()[0]


def get_post_by_user_id(user_id: int):
    statement: str = ''' SELECT * FROM posts WHERE user_id=? '''
    c.execute(statement, (user_id, ))
    return c.fetchall()
