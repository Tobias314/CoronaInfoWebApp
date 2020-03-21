import sqlite3
import os
import config
from database.databaseconnection import DatabaseConnection

if os.path.exists(config.DATABASE_PATH):
    os.remove(config.DATABASE_PATH)

db = DatabaseConnection()
c = db.cursor

# Create district table
c.execute('''CREATE TABLE Districts
             (name text)''')
# Insert district data
c.execute("INSERT INTO Districts VALUES ('Potsdam')")
c.execute("INSERT INTO Districts VALUES ('Berlin Mitte')")
c.execute("INSERT INTO Districts VALUES ('Berlin Steglitz-Zehlendorf')")
c.execute("INSERT INTO Districts VALUES ('Potsdam')")

c.execute("INSERT INTO Districts VALUES ('Altmarkkreis Salzwedel')")
c.execute("INSERT INTO Districts VALUES ('Anhalt-Bitterfeld')")
c.execute("INSERT INTO Districts VALUES ('Börde')")
c.execute("INSERT INTO Districts VALUES ('Burgenlandkreis')")
c.execute("INSERT INTO Districts VALUES ('Harz')")
c.execute("INSERT INTO Districts VALUES ('Jerichower Land')")
c.execute("INSERT INTO Districts VALUES ('Mansfeld-Südharz')")
c.execute("INSERT INTO Districts VALUES ('Saalekreis')")
c.execute("INSERT INTO Districts VALUES ('Salzlandkreis')")
c.execute("INSERT INTO Districts VALUES ('Stendal')")
c.execute("INSERT INTO Districts VALUES ('Wittenberg')")
c.execute("INSERT INTO Districts VALUES ('Dessau-Roßlau')")
c.execute("INSERT INTO Districts VALUES ('Halle')")
c.execute("INSERT INTO Districts VALUES ('Magdeburg')")

c.execute('''CREATE TABLE DistrictCaseNumbers
             (district_name text, source_url text, case_number integer, data_time_stamp text)''')

db.commit()
