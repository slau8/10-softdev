'''
itch4stitch
Shannon Lau and Jennifer Zhang
SoftDev1 pd 7
HW10 -- Average
2017-10-16
'''

import sqlite3, csv

f = "discobandit.db"
db = sqlite3.connect(f) # open if f exists, otherwise create
c = db.cursor() # facilitate db ops

gradebook = {} # stores id, name, and marks

# ============CREATE AND POPULATE TABLES============
def initiate():
    # create peeps and courses tables
    c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
    # populate tables
    peeps = csv.DictReader(open("peeps.csv"))
    for row in peeps:
        c.execute("INSERT INTO peeps VALUES (?,?,?)",(row['name'], row['age'], row['id']))
    courses = csv.DictReader(open("courses.csv"))
    for row in courses:
        c.execute("INSERT INTO courses VALUES (?,?,?)",(row['code'], row['mark'], row['id']))

# ============CREATE AND UPDATE GRADEBOOK============
def create_gradebook():
    # create [][] with name | id | mark (for each class of each person)
    data = c.execute('''SELECT name,peeps.id,mark
                        FROM peeps,courses
                        WHERE peeps.id = courses.id''')
    for student in data: # student is a list
        add_mark(student) # add mark to student's grade
    print '\n\n\nINITIALIZED GRADEBOOK:\n'
    print gradebook

def update_gradebook(this_code, this_key):
    # create [][] with name | id | mark (for the new mark to be added)
    data = c.execute('''SELECT name,peeps.id,mark
                        FROM peeps,courses
                        WHERE peeps.id = courses.id
                            AND courses.id = ?
                            AND courses.code = ?''', (this_key, this_code))
    for student in data: # student is a list
        add_mark(student) # add mark to gradebook{}
    print '\n\n\nUPDATED GRADEBOOK:\n'
    print gradebook

# add mark to gradebook{}
def add_mark(student):
    # {id: [name, mark1, mark2, mark3], ...}
    name = student[0]
    key = student[1] # student id
    mark = student[2]
    if key in gradebook:
        gradebook[key].append(mark) # if student exists in dict, add the mark to the list
    else:
        gradebook[key] = [name, mark] # else, create a list with a name and mark

# ============CREATE AND UPDATE TABLE============
# create and print table of peeps_avg
def create_peepsavg():
    create_gradebook() # initialize gradebook{}
    c.execute("CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, average NUMERIC)")
    print '\n\n\nINITIAL TABLE WITH AVERAGES:\n'
    for student in gradebook:
        key = student # student id
        name = gradebook[student][0]
        average = avg(student)
        print name + ", " + str(key) + ", " + str(average)
        c.execute("INSERT INTO peeps_avg VALUES(?,?)",(key, average))

# update and print table of peeps_avg
def update_peepsavg():
    print '\n\n\nUPDATED TABLE WITH AVERAGES:\n'
    for student in gradebook:
        key = student # student id
        name = gradebook[student][0]
        this_average = avg(student)
        print name + ", " + str(key) + ", " + str(this_average)
        c.execute("UPDATE peeps_avg SET average = ? WHERE id = ?", (this_average, key))

# find average of student marks
def avg(student):
    scores = gradebook[student][1:] # list of student scores
    return sum(scores) * 1.0 / len(scores) # calculate average

# ============ADD COURSE GRADE============
def add_grade(code, mark, key):
    # add values to courses table
    c.execute("INSERT INTO courses VALUES(?,?,?)",(code, mark, key))
    update_gradebook(code, key)



def main():
    initiate() # import data from peeps and courses
    create_peepsavg() # create table with averages
    add_grade('graphics',85,4)
    update_peepsavg() # update table with averages

main()

db.commit() # save changes
db.close() # close database
