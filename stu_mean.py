'''
Shannon Lau and Jennifer Zhang
SoftDev1 pd 7
HW10 -- Average
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

c.execute("CREATE TABLE averages (name TEXT, id INTEGER, average INTEGER)")
temp = 0 # previous id
count = 0 # counts number of classes per student
total = 0 # sum of student's marks
for bar in foo:
    if temp == bar[1]:
        
    
    
    
db.commit() #save changes
db.close()  #close database

