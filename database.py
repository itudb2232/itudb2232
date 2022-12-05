import sqlite3 as dbapi2

from ships import Ships


class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile  

    def add_ship(self, ship):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO SHIPS (NAME, TYPE, ACTIVE) VALUES (?, ?, ?)"
            cursor.execute(query, (ship.name, ship.type, ship.active))
            connection.commit()
            ship_key = cursor.lastrowid
        return ship_key

    def update_ship(self, ship_key, ship):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE SHIPS SET NAME = ?, TYPE = ? , ACTIVE = ? WHERE (SHIP_ID = ?)"
            cursor.execute(query, (ship.name, ship.type, ship.active, ship_key))
            connection.commit()

    def delete_ship(self, ship_key):
        print("Type your code below! indentation is important!!!")
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM SHIPS WHERE (SHIP_ID = ?)"
            cursor.execute(query, (ship_key,))
            connection.commit()

    def get_ship(self, ship_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT NAME, TYPE, ACTIVE FROM SHIPS WHERE (SHIP_ID = ?)"
            cursor.execute(query, (ship_key,))
            name, type, active = cursor.fetchone()
        ship_ = Ships(name,type,active,)
        return ship_

    def get_ships(self):
        ships = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT SHIP_ID, NAME, TYPE, ACTIVE FROM SHIPS ORDER BY SHIP_ID"
            cursor.execute(query)
            for ship_key, ship_id,name, type, active in cursor:
                ships.append((ship_key, Ships(ship_id,name, type, active)))
        return ships