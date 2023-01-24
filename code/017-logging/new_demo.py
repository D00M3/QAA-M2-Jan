def changeData(data):
    data.setAttribute()
    if data.colour == "red":
        print("triggered")

    print(data)
    return data

def returnNumber():
    return 123

# If this code is published and other people use it, there will 
#be mystery print() happening they're not clear where they are clearing

# Logging is the same as printing, but using a dedicate 'logger'
# Logging you can set the 'value' of a log
# DEBUG, INFO, WARNING, ERROR, CRITICAL

import logging
import os
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# Creating a logger called newLogger
newLog = logging.getLogger("newLog") 
newLog.setLevel(logging.DEBUG)

newHandler = logging.FileHandler('cool_logs.txt')
newLog.addHandler(newHandler) 
# Set the handler of newLog to be our fileHandler

newLog.info(returnNumber())
newLog.critical("Hello World")