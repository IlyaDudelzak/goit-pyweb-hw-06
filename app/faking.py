from connection import create_connection
from datetime import datetime, timedelta
from random import randint, randrange
from pathlib import Path

import adapters
import sqlite3
import faker
import time

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 1000

def executeScriptsFromFile(filename):
    with sqlite3.connect('db.db') as con:
        cur = con.cursor()
        # Open and read the file as a single buffer
        fd = open(filename, encoding="utf-8")
        sqlFile = fd.read()
        fd.close()

        # all SQL commands (split on ';')
        sqlCommands = sqlFile.split(';')

        # Execute every command from the input file
        for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                cur.execute(command)
            except Exception:
                pass
    
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def generate_fake_data() -> tuple():
    fake_students = []
    fake_groups = []
    fake_teachers = []
    fake_subjects = []
    fake_data = faker.Faker("ru_RU")
    for _ in range(NUMBER_STUDENTS):
        fake_students.append(fake_data.name())
    for _ in range(NUMBER_GROUPS):
        fake_groups.append(fake_data.word())
    for _ in range(NUMBER_TEACHERS):
        fake_teachers.append(fake_data.name())
    for _ in range(NUMBER_SUBJECTS):
        fake_subjects.append(fake_data.job())

    return fake_groups, fake_students, fake_subjects, fake_teachers

def insert_data_to_db(groups, students, disciplines, teachers) -> None:
    with create_connection() as con:
        cur = con.cursor()
        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        for group in groups:
            cur.execute(sql_to_groups, (group,))
        con.commit()
        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?, ?)"""
        for student in students:
            cur.execute(sql_to_students, (student, randint(1, NUMBER_GROUPS)))
        con.commit()
        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                              VALUES (?)"""
        for teacher in teachers:
            cur.execute(sql_to_teachers, (teacher,))
        con.commit()
        sql_to_subjects = """INSERT INTO disciplines(subject_name, teacher_id)
                              VALUES (?, ?)"""
        for discipline in disciplines:
            cur.execute(sql_to_subjects, (discipline, randint(1, NUMBER_TEACHERS)))
        con.commit()
        sql_to_subjects = """INSERT INTO disciplines(subject_name, teacher_id)
                              VALUES (?, ?)"""
        for discipline in disciplines:
            cur.execute(sql_to_subjects, (discipline, randint(1, NUMBER_TEACHERS)))
        con.commit()
        sql_to_grades = """INSERT INTO grade(grade, grade_date, student_id, discipline_id)
                              VALUES (?, ?, ?, ?)"""
        for i in range(NUMBER_GRADES):
            cur.execute(sql_to_grades, (randint(2, 12), random_date(datetime(2010, 1, 1, 0, 0, 0, 0), datetime.now()), randint(1, NUMBER_STUDENTS), randint(1, NUMBER_SUBJECTS)))

def fake_fill():
    insert_data_to_db(*generate_fake_data())