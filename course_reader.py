__author__ = 'Miranda'
import csv
import sqlite3

def load_course_database(db_name, csv_filename):
    with open(csv_filename, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                t = tuple(row)
            
    conn = sqlite3.connect(db_name)
    with conn:
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
        cur.execute(sql_cmd, t) #value of dept used for the first ?, and courseNum for the 2nd


if __name__ == '__main__':
    load_course_database('course1.db', 'seas-courses-5years.csv')
