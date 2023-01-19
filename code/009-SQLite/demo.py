import sqlite3 as sql

# Connection - Where is the database stored, and any passwords needed
# Cursor - Virtual tool to navigate a DB 
# Query - What request / query are we sending to the DB 

# Connect to test-db, if it doesn't exist it creates it  
conn = sql.connect("choc-db")

# Create our cursor, which is a function which is part of connection
cursor = conn.cursor()

# Python is reading our sql file and saving a String of content
# sql_file = open("chocolate.sql")
# sql_string = sql_file.read()
# Python is running this SQL string inside of our DB 
# cursor.executescript(sql_string)

def runQuery(query):
    data = cursor.execute(query).fetchall()
    return data

def addChoc():
    insert_str = "INSERT INTO chocolate (flavour, weight_gr, fairtrade) VALUES ('Pistachio', 67, true);"
    runQuery(insert_str)
    return True

def updateChocFlavour(id, value):
    update_query = f"UPDATE chocolate SET flavour = '{value}' WHERE choc_id = {id}"
    runQuery(update_query)
    return True

addChoc()
updateChocFlavour(2, "latte")

 

# Run some type of query 
# query_str = "SELECT * FROM sqlite_schema;"
# db_data = cursor.execute(query_str).fetchall()
# print(db_data)

# Saving the data into the db created via cursor stuff
conn.commit()

