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
    def delete(cls, id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from users where id= {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

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
