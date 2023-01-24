import sqlite3 as sql

conn = sql.connect("zoo-db")

cursor = conn.cursor()

def setupTable():
    sql_file = open("penguins.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)

def runQuery(query):
    data = cursor.execute(query).fetchall()
    return data

def viewAllRecords():
    query = "SELECT * FROM penguins;"
    data = runQuery(query)
    return data

def createPenguin(fish_eaten, dancing, name):
    query = f"INSERT INTO penguins (fish_eaten, dancing, penguin_name) VALUES ({fish_eaten}, {dancing}, '{name}');"
    runQuery(query)
    return True

def commitChanges():
    conn.commit()

# Uncomment this and run the file once to set up the DB
# setupTable()



# createPenguin(20, True, 'Toni')
# print(viewAllRecords())

conn.commit()
