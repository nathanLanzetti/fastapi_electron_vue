import sqlite3
from sqlite3 import Error
from datetime import datetime
from os.path import join
import os

TABLES = {
    'users': (
        "CREATE TABLE IF NOT EXISTS `users` ("
        "  `user_id` integer PRIMARY KEY,"
        "  `firstname` varchar(100) NOT NULL,"
        "  `lastname` varchar(100) NOT NULL,"
        "  `pseudo` varchar(100) NOT NULL"
        ");"
    ),
    'posts': (
        "CREATE TABLE IF NOT EXISTS `posts` ("
        "  `post_id` integer PRIMARY KEY,"
        "  `content` varchar(200) NOT NULL,"
        "  `upvotes` integer NOT NULL,"
        "  `downvotes` integer NOT NULL,"
        "  `begin_date` text NOT NULL,"
        "  `user_id` integer NOT NULL,"
        "  FOREIGN KEY (`user_id`) REFERENCES users(`user_id`)"
        # "  ON UPDATE SET NULL,"
        # "  ON DELETE SET NULL,"
        ");"
    ),
}

USERS = {
    1: ("Nathan", "Lanzetti", "YellowTea_12"),
    2: ("Kiki", "Poulet", "Larceny"),
    3: ("Mel", "Tib", "Holie"),
}

POSTS = {
    1: ("This is the first post.", 0, 0, datetime.now(), 1),
    2: ("This is the second post.", 18, 7, datetime.now(), 2),
    3: ("Read the reddit post.", 10, 1, datetime.now(), 2),
    4: ("Greatsword is the best !", 77, 0, datetime.now(), 2),
    5: ("Charge blade is kinda disapointing..", 0, 20, datetime.now(), 3),
    6: ("Don't wanna fight Nergigante", 5, 30, datetime.now(), 3),
}


def init_database_reddit(db_file):
    print(db_file)
    conn = __create_connection(db_file)
    __create_tables(conn)
    __create_users(conn)
    __create_posts(conn)


def __create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    print(f"{conn} and {db_file}")
    return conn


def __create_tables(conn, tables=TABLES):
    cursor = conn.cursor()
    for name in tables:
        query = tables[name]
        try:
            print(f"Table {name} was created.")
            cursor.execute(query)
        except Error as err:
            print(f"Error: {err.args[0]}")


def __create_user(conn, user):
    """
    Create a new user into the projects table
    """
    print(f"User : {user}")
    sql = ''' INSERT INTO users(firstname,lastname,pseudo)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid


def __create_users(conn, users=USERS):
    """
    Create a new user into the projects table
    """
    lists_of_ids = []
    for user_number in users:
        lists_of_ids.append(__create_user(conn, users[user_number]))
    return lists_of_ids


def __create_post(conn, post):
    """
    Create a new user into the projects table
    """
    sql = ''' INSERT INTO posts(content, upvotes, downvotes, begin_date, user_id)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, post)
    conn.commit()
    return cur.lastrowid


def __create_posts(conn, posts=POSTS):
    """
    Create a new user into the projects table
    """
    list_of_ids = []
    for post_number in posts:
        list_of_ids.append(__create_post(conn, posts[post_number]))
    return list_of_ids


# if __name__ == '__main__':
#     run()
