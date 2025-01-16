DROP TABLE IF EXISTS students; 
CREATE TABLE students (
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name STRING,
     group_id REFERENCES [groups] (id)
);