# CSCI 2061,
# Abiola Adimi

#Import sqlite3 lib
import sqlite3


def main():
    #Initializes studentList.
    studentList = [ ('Ann Annson', 19, 'Freshman', 3.0),
                    ('Bill Billson', 20, 'Sophmore', 3.4),
                    ('Carl Carlson', 21, 'Junior', 4.0),
                    ('Dawn Dawnson', 22, 'Senior', 2.7)]

    again = 'Y'

    #Creates a database
    db = sqlite3.connect('studentList.db')  

    #Creates table with studentList and initializes it with values.
    db.execute('drop table if exists students')
    db.execute('create table students (name text, age int, year text, gpa float)')
    db.executemany('insert into students (name, age, year, gpa) values (?, ?, ?, ?)', (studentList))
    db.commit()

    #Dislpays the table created in the datebase.
    print('After creation database is:')
    cursor = db.execute('select * from students order by name, age, year, gpa')
    for r in cursor:
        print(r)
        
    print()

    #Inserting new data into the table.
    while (again == 'Y' or again == 'y'):
        name = input('Please enter student name: ')
        age = input('Please enter student age: ')
        year = input('Please enter student year: ')
        gpa = input('Please enter student GPA: ')
        db.execute('insert into students(name, age, year, gpa) values (?, ?, ?, ?)', (name, age, year, gpa))
        db.commit
        again = input('Go again? ')

    print()

    #Displays the table after inserting data.
    print('After additions, database is:')
    cursor = db.execute('select * from students order by name, age, year, gpa')
    for r in cursor:
        print(r)

    print()
    
    #Searches inside of the table and displays that data.
    name = (input('Student to search for? '),)
    cursor = db.execute('select *from students where name = ?', name)
    print(cursor.fetchone())
    
    print()

    #Deletes data from the table.
    name = (input('Student to delete? '),)
    cursor = db.execute('delete from students where name = ?', name)
    db.commit()
    
    print()

    #Displays the table after data has been deleted.
    print('After deletion, database is:')
    cursor = db.execute('select * from students order by name, age, year, gpa')
    for r in cursor:
        print(r)

    #Closes the database file.
    db.close()
    
if __name__ == "__main__": main()
