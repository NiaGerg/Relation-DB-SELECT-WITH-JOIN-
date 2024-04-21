import sqlite3


conn = sqlite3.connect('sqlite3.db')


cursor = conn.cursor()


cursor.executescript(''' 
CREATE TABLE Advisor( 
    AdvisorID INTEGER PRIMARY KEY, 
    AdvisorName TEXT NOT NULL
); 

CREATE TABLE Student( 
    StudentID INTEGER PRIMARY KEY, 
    StudentName TEXT NOT NULL
); 

CREATE TABLE Student_Advisor(
    StudentID INTEGER,
    AdvisorID INTEGER,
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
    PRIMARY KEY(StudentID, AdvisorID)
);
''')


cursor.executescript('''
INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES 
(1,"John Paul"), 
(2,"Anthony Roy"), 
(3,"Raj Shetty"), 
(4,"Sam Reeds"), 
(5,"Arthur Clintwood"); 

INSERT INTO Student(StudentID, StudentName) VALUES 
(501,"Geek1"), 
(502,"Geek2"), 
(503,"Geek3"), 
(504,"Geek4"), 
(505,"Geek5"), 
(506,"Geek6"), 
(507,"Geek7"), 
(508,"Geek8"), 
(509,"Geek9"), 
(510,"Geek10"); 

INSERT INTO Student_Advisor(StudentID, AdvisorID) VALUES
(501, 1),
(502, 1),
(503, 3),
(504, 2),
(505, 4),
(506, 2),
(507, 2),
(508, 3),
(509, 1),
(510, 1);
''')


conn.commit()


def get_advisors_with_students():
    query = '''
    SELECT Advisor.AdvisorName, COUNT(Student_Advisor.StudentID) AS NumberOfStudents
    FROM Advisor
    LEFT JOIN Student_Advisor ON Advisor.AdvisorID = Student_Advisor.AdvisorID
    GROUP BY Advisor.AdvisorName;
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


advisors_with_students = get_advisors_with_students()
for advisor in advisors_with_students:
    print(f"Advisor: {advisor[0]}, Number of Students: {advisor[1]}")


conn.close()
