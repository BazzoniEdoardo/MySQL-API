import mysql.connector

#Metodo Connect per connettersi ad un database, mettere la funzione all'interno di una variabile per avere la connessione
def connect(host, user, psw, database):
    if database == None or "":
        try:
            db = mysql.connector.connect(
                host=host,
                user=user,
                password=psw
            )
            print(f"Connected to MySQL | Host: {host} | User: {user}")
            return db
        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")
    else:
        try:
            db = mysql.connector.connect(
                host=host,
                user=user,
                password=psw,
                database=database
            )
            print(f"Connected to MySQL | Host: {host} | User: {user} | Database: {database}")
            return db
        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")


def create_database(connection, database):
    try:
        cur = connection.cursor()
        cur.execute(f"CREATE DATABASE {database}")
        print(f"Database '{database}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def check_database(connection, database):
    try:
        cur = connection.cursor()
        cur.execute("SHOW DATABASES")
        database = (f"{database}",)
        y = True

        for x in cur:
            if x != database:
                y = False
            else:
                y = True
                break

        return y
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
                

def create_table(connection, table, param):
    try:
        cur = connection.cursor()
        cur.execute(f"CREATE TABLE {table} ({param})")
        print(f"Table '{table}' created successfully! ")
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def insert(connection, table, param, values):
    try:
        cur = connection.cursor()
        cur.executemany(f"INSERT INTO {table} ({param}) VALUES (%s, %s)", values)
        connection.commit()
        print(cur.rowcount, "record inserted!")

    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def select(connection, table, param):
    try:
        cur = connection.cursor()
        cur.execute(f"SELECT {param} FROM {table}")
        return cur.fetchall()
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def delete(connection, table, param, value):
    try:
        cur = connection.cursor()
        cur.execute(f"DELETE FROM {table} WHERE {param} = '{value}'")
        connection.commit()
        print(f"Deleted {value} from {param} in {table}| {cur.rowcount} record(s) deleted")
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def delete_table(connection, table):
    try:
        cur = connection.cursor()
        cur.execute(f"DROP TABLE {table}")
        print(f"Table {table} deleted!")
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def update(connection, table, param, before, after):
    try:
        cur = connection.cursor()
        cur.execute(f"UPDATE {table} SET {param} = '{after}' WHERE {param} = '{before}'")
        connection.commit()
        print(cur.rowcount, f"record(s) affected! From: {before} to {after}")
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def show_database(connection):
    try:
        cur = connection.cursor()
        cur.execute("SHOW DATABASES")
        z = ()
        for x in cur:
            z = z + x
        return z
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def show_tables(connection):
    try:
        cur = connection.cursor()
        cur.execute("SHOW TABLES")
        z = ()
        for x in cur:
            z = z + x
        return z
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


# conn = connect("localhost", "root", "", "jamal")
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple st 652')
# ]
# insert(conn, "customers", "name, address", val)
# create_table(conn, "pierino", "name VARCHAR(255), address VARCHAR(255)")
# print(select(conn, "customers", "*"))
# delete(conn, "customers", "address", "Lowstreet 4")
# delete_table(conn, "pierino")
# update(conn, "customers", "name", "Amy", "Melinda")
# print(show_database(conn))
# print(show_tables(conn))
