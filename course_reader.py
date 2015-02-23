__author__ = 'Miranda'
import csv
import sqlite3

def load_course_database(db_name, csv_filename):
    print("hello")
    with open(csv_filename, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
    conn = sqlite3.connect(db_name)
    with conn:
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values(?, ?, 1122, 'Lecture', 20, 20, 'T. Jefferson')"
        cur.execute(sql_cmd, (dept,courseNum)) #value of dept used for the first ?, and courseNum for the 2nd


if __name__ == '__main__':
    print("hello")
    load_course_database('course1', 'seas-courses-5years.csv')
