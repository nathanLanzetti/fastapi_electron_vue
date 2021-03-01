import init_database_reddit as init_database

TABLES = {
    'monsters': (
        "CREATE TABLE IF NOT EXISTS `monsters` ("
        "  `monster_id` integer PRIMARY KEY,"
        "  `name` varchar(100) NOT NULL,"
        "  `description` text NOT NULL,"
        "  `hp` integer NOT NULL"
        ");"
    ),
    'weapons': (
        "CREATE TABLE IF NOT EXISTS `weapons` ("
        "  `weapons_id` integer PRIMARY KEY,"
        "  `name` varchar(200) NOT NULL,"
        "  `rank` integer NOT NULL,"
        "  `dmg` integer NOT NULL"
        ");"
    ),
}

MONSTERS = {
    1: ("Diablos", "A flying wyvern that can burrows in the ground.", 6000),
    2: ("Kirin", "An elder dragon looking like a unicorn that can dish out ligthning attacks", 4500),
    3: ("Zorah Magdaros", "Mysterious Wyvern that can destroy an entire ecosystem", 20000),
}

WEAPONS = {
    1: ("Greatsword", 1, 1000),
    2: ("Charge Blade", 2, 800),
    3: ("Insect Glaive", 7, 550),
    4: ("Switch Axe", 8, 750),
    5: ("Sword and Shield", 4, 285),
    6: ("Hunting Horn", 14, 625),
}


def init_database_monster(db_file):
    conn = init_database.__create_connection(db_file)
    init_database.__create_tables(conn, TABLES)
    __create_monsters(conn)
    __create_weapons(conn)


def __create_monster(conn, monster):
    """
    Create a new monster into the projects table
    """
    sql = ''' INSERT INTO monsters(name,description,hp)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, monster)
    conn.commit()
    return cur.lastrowid


def __create_monsters(conn, monsters=MONSTERS):
    """
    Create a new monster into the projects table
    """
    lists_of_ids = []
    for monster_number in monsters:
        lists_of_ids.append(__create_monster(conn, monsters[monster_number]))
    return lists_of_ids


def __create_weapon(conn, weapon):
    """
    Create a new user into the projects table
    """
    sql = ''' INSERT INTO weapons(name, rank, dmg)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, weapon)
    conn.commit()
    return cur.lastrowid


def __create_weapons(conn, weapons=WEAPONS):
    """
    Create a new weapon into the projects table
    """
    list_of_ids = []
    for weapon_number in weapons:
        list_of_ids.append(__create_weapon(conn, weapons[weapon_number]))
    return list_of_ids
