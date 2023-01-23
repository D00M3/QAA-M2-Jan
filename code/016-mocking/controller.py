import service
import db

def startApp():
    print(menu)
    exit = False
    while not exit:
        choice = input("Please select a choice: ")
        if choice == "1":
            print(readAll())
        elif choice == "2":
            print(readOne())
        else:
            exit = True
            db.commitChanges()

def readAll():
    return service.getAll()

def readOne():
    id = input("Please enter penguin ID to read: ")
    return service.getOne(id)


menu = """
    Welcome to Penguin DB! 
    Please select a choice from below: 
    1. Read All 
    2. Read By ID
    2. Create a Penguin
    3. Exit
    """

startApp()
    