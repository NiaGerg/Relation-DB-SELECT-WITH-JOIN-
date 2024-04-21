QLite Many-to-Many Relationship for Students and Advisors

This Python script demonstrates how to model a many-to-many relationship between students and advisors using a join table in a SQLite database.

Functionality:

Creates three tables: Advisor, Student, and Student_Advisor (join table).
Defines primary and foreign keys for data integrity.
Inserts sample data into the tables, demonstrating the many-to-many relationship.
Provides a function get_advisors_with_students to retrieve advisors and their student count.
Prints a list of advisors with the number of students they advise.
Requirements:

Python 3 (tested with 3.x)
sqlite3 module