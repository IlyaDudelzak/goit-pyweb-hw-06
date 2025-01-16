DROP TABLE IF EXISTS grade; 
CREATE TABLE grade (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    grade INTEGER, 
    discipline_id REFERENCES disciplines (id),
    student_id REFERENCES students (id),
    date_of DATE
);