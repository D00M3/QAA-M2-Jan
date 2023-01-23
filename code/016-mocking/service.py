import db

def getAll():
    data = db.viewAllRecords()
    return data

def getOne(id):
    query = f"SELECT * FROM penguins WHERE penguin_id = {id}"
    data = db.runQuery(query)
    return data # Returning data that is being fetched from db.py

def createPenguin(fish, dancing, name):
    query = f"INSERT INTO penguins (fish_eaten, dancing, penguin_name) VALUES ({fish}, {dancing}, '{name}');"
    db.runQuery(query)
    return True

def deletePenguin(id):
    query = f"DELETE FROM penguins WHERE id = {id}"
    db.runQuery(query)
    return True

