from app import mysql


class Students(object):
    def __init__(
        self,
        id=None,
        firstname=None,
        lastname=None,
        coursecode=None,
        year=None,
        gender=None,
    ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.coursecode = coursecode
        self.year = year
        self.gender = gender

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO students(id, firstname, lastname, coursecode, year, gender) \
            VALUES('{self.id}', '{self.firstname}', '{self.lastname}', '{self.coursecode}', '{self.year}', '{self.gender}')"
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls, student_id):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM students WHERE id = %s"
            cursor.execute(sql, (student_id,))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting student: {e}")
            return False
        finally:
            cursor.close()

    @classmethod
    def edit(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM students WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def update(cls, id, firstname, lastname, coursecode, year, gender):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE students
            SET id = %s,
                firstname = %s,
                lastname = %s,
                coursecode = %s,
                year = %s,
                gender = %s
            WHERE id = %s
            """,
            (id, firstname, lastname, coursecode, year, gender),
        )
        mysql.connection.commit()
