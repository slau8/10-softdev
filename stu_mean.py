'''
Shannon Lau
SoftDev1 pd 7
HW09 -- No Treble
2017-10-16
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

# Create table for 'peeps' data
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
peeps = csv.DictReader(open("peeps.csv"))
# Inserts data into 'peeps' table
for row in peeps:
    c.execute("INSERT INTO peeps VALUES ('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ")")

# Create table for 'courses' data
'''
Shannon Lau
SoftDev1 pd 7
HW09 -- No Treble
2017-10-16
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

# Create table for 'peeps' data
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
peeps = csv.DictReader(open("peeps.csv"))
# Inserts data into 'peeps' table
for row in peeps:
    c.execute("INSERT INTO peeps VALUES ('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ")")

# Create table for 'courses' data
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
courses = csv.DictReader(open("courses.csv"))
# Inserts data into 'course' table
for row in courses:
    c.execute("INSERT INTO courses VALUES ('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ")")

foo = c.execute("SELECT name,peeps.id,mark FROM peeps,courses WHERE peeps.id = courses.id")

print foo

for bar in foo:
    
    
db.commit() #save changes
db.close()  #close database
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
courses = csv.DictReader(open("courses.csv"))
# Inserts data into 'course' table
for row in courses:
    c.execute("INSERT INTO courses VALUES ('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ")")

foo = c.execute("SELECT name,peeps.id,mark FROM peeps,courses WHERE peeps.id = courses.id")

for bar in foo:
    print bar[0]

'''
Shannon Lau
SoftDev1 pd 7
HW09 -- No Treble
2017-10-16
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

# Create table for 'peeps' data
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
peeps = csv.DictReader(open("peeps.csv"))
# Inserts data into 'peeps' table
for row in peeps:
    c.execute("INSERT INTO peeps VALUES ('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ")")

# Create table for 'courses' data
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
courses = csv.DictReader(open("courses.csv"))
# Inserts data into 'course' table
for row in courses:
    c.execute("INSERT INTO courses VALUES ('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ")")

foo = c.execute("SELECT name,peeps.id,mark FROM peeps,courses WHERE peeps.id = courses.id")

print foo

for bar in foo:
    
    
db.commit() #save changes
db.close()  #close database


db.commit() #save changes
db.close()  #close database
