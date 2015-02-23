__author__ = 'Miranda'
import csv
import sqlite3

def load_course_database(db_name, csv_filename):
    with open(csv_filename, 'rU') as csvfile:
            reader = csv.reader(csvfile)
         #   for row in reader:
          #      print(row[0])
           #     print(row[1])
            #    print(row[2])
             #   print(row[3])

    print(tuple(reader))


    conn = sqlite3.connect(db_name)
    with conn:
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values(?, ?, 1122, 'Lecture', 20, 20, 'T. Jefferson')"
        cur.execute(sql_cmd, (dept,courseNum)) #value of dept used for the first ?, and courseNum for the 2nd


if __name__ == 'main':
    load_course_database('data', 'seas-courses-5years.csv')
