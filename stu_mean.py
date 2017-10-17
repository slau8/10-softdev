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

students = c.execute("SELECT name,peeps.id,mark FROM peeps,courses WHERE peeps.id = courses.id")
# for student in students:
#     print(student)

#c.execute("CREATE TABLE averages (name TEXT, id INTEGER, average INTEGER)")
first_id = True #checks to see if its the first occurence of that id
curr_id = 0 # current id
count = 0 # counts number of classes per student
total = 0 # sum of student's marks

averages = {'id': 'average'}
for student in students:
    #if student[1] == 1 or (student[1] == 2 and student[2] == 65):
        #print(student)
        if first_id:
            curr_id = student[1]
            first_id = False
            #print('ran first_id')
        if curr_id == student[1]:
            total += student[2]
            count+=1
            #print('ran curr_id')
        else:
            averages[curr_id] = total / count
            #print(total)
            #print(count)

            count = 0
            total = 0
            first_id = True
            #print('ran else')

print (averages)

db.commit() #save changes
db.close()  #close database
