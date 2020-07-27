import sqlite3
from sqlite3 import Error


def connect(db):
    exit = None
    exit = sqlite3.connect(db)

    if exit:
        print("connected succesfully")
    else:
        print("erreur opening database")

    return exit

def creat_table(exit):
    sql = """CREATE TABLE IF NOT EXISTS BOOKS (
    ID integer PRIMARY KEY ,
    Nom text NOT NULL,
    Auteur text NOT NULL,
    Prix integer NOT NULL,
    Quantiter integer NOT NULL
    );"""
    sql1 = """CREATE TABLE IF NOT EXISTS ADMIN (
      id integer PRIMARY KEY,
      username text NOT NULL,
      passe text NOT NULL
      );"""
    try:
        cur = exit.cursor()
        cur.execute(sql)
        cur.execute(sql1)
        print("created succesfully")
    except Error as e:
        print(e)


def full_table(exit):
    sql = """INSERT INTO ADMIN(id,username,passe) VALUES (1,'admin','admin')"""

    cur = exit.cursor()
    cur.execute(sql)
    exit.commit()


