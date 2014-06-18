import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" %(first_name, last_name)

def get_project_description(project_title):
    query = """SELECT title, description FROM Projects WHERE title=(?) """
    DB.execute(query, (project_title,))
    row = DB.fetchone()
    print """\
Project: %s 
Project Description: %s""" % (row[0], row[1])


def make_new_project(title, description, max_grade):
    query = """INSERT INTO Projects (title, description, max_grade) VALUES (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added Project: %s" %title

def main():
    connect_to_db()
    command = None
    argument_list = []
    
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        temp_arg_list = input_string.split()
        if temp_arg_list[0]=="new_project":
            new_input_string = input_string.split("\"")
            first_two_args = new_input_string[0].split()

            first_two_args.append(new_input_string[1])
            first_two_args.append(new_input_string[2])
    
            argument_list = first_two_args
            command = argument_list[0]
            args = argument_list[1:]

        else:
            tokens = input_string.split()
            command = tokens[0]
            args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "Projects":
            get_project_description(*args) 
        elif command == "new_project":
            make_new_project(*args)   

    CONN.close()

if __name__ == "__main__":
    main()
