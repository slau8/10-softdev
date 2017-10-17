'''
Shannon Lau and Jennifer Zhang
SoftDev1 pd 7
HW10 -- Average
2017-10-16
'''

import sqlite3, csv

f = "discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()

# ============CREATE AND POPULATE TABLES============
# create peeps and courses tables
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

# populate tables
peeps = csv.DictReader(open("peeps.csv"))
for row in peeps:
    c.execute("INSERT INTO peeps VALUES ('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ")")
courses = csv.DictReader(open("courses.csv"))
for row in courses:
    c.execute("INSERT INTO courses VALUES ('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ")")

# ============COLLECT EACH STUDENT'S GRADE============
# create [][] with name | id | mark
data = c.execute("SELECT name,peeps.id,mark FROM peeps,courses WHERE peeps.id = courses.id")
print data

# create {id: [name, mark1, mark2, mark 3], ...}
gradebook = {}
for student in data:
    name = student[0]
    key = student[1] # student id
    mark = student[2]
    if key in gradebook:
        gradebook[key].append(mark) # add the mark to the list
    else:
        gradebook[key] = [name, mark] # create a list with a name and mark

print 'GRADEBOOK: '
print gradebook

# ============CALCULATE AVERAGE AND DISPLAY============
print "STUDENTS' AVERAGES: "
print "\n"
for student in gradebook:
    key = student # student id
    name = gradebook[student][0]
    scores = gradebook[student][1:] # list of student scores
    average = sum(scores) * 1.0 / len(scores)
    print name + ", " + str(key) + ", " + str(average)


db.commit() #save changes
db.close()  #close database
