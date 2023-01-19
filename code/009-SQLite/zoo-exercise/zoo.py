import sqlite3 as sql

conn = sql.connect("zoo-db")

cursor = conn.cursor()

def setupTable():
    sql_file = open("penguins.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)

def runQuery(query):
    data = cursor.execute(query)
    return data

def viewAllRecords():
    query = "SELECT * FROM penguins;"
    data = runQuery(query).fetchall()
    return data

def createPenguin(fish_eaten, dancing, name):
    query = f"INSERT INTO penguins (fish_eaten, dancing, penguin_name) VALUES ({fish_eaten}, {dancing}, '{name}');"
    runQuery(query)
    return True

print(
    """
    Welcome to Penguin DB! 
    Please select a choice from below: 
    1. Read All 
    2. Create a Penguin
    3. Exit
    """
)
exit = False
while exit == False:
    choice = input("Please select a choice (number): ")
    if choice == "1":
        print(viewAllRecords())
    elif choice == "2":
        fish_eaten = int(input("Please specify how mant fish eaten: "))
        createPenguin(fish_eaten, True, "Toni")
    else:
        exit = True

# createPenguin(20, True, 'Toni')
# print(viewAllRecords())

conn.commit()
