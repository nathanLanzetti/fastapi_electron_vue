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
    statement = ''' INSERT INTO monsters(name, description, hp)
                    VALUES (?,?,?)'''
    c.execute(statement, tuple(monster_to_create.values()))
    c.commit()
    return c.lastrowid
