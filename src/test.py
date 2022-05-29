from dataclasses import dataclass
import mysql.connector
from mysql.connector import Error
from modules import db
import random

# Get the port types and store them in a list.
portclass = []
ports = 10
connection = db.stdb()
query = "select * from `portclass`"
presults = db.query(connection, query)
for prow in presults:
    tempportclass = [prow['portclass'], prow['orecap'],
                     prow['organicscap'], prow['equipmentcap']]
    portclass.append(tempportclass)

print(portclass[0])
portclass.pop(0)
print(portclass[0])

# * Determine if there will be a port around this planet.
portrand = random.randrange(0, 100)
if int(ports) <= portrand:
    # Randomly pick the class
    portclassval = random.randrange(0, len(portclass))
