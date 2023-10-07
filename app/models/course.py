from app import mysql


class Courses(object):
    def __init__(self, code=None, name=None, collegecode=None):
        self.code = code
        self.name = name
        self.collegecode = collegecode

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO courses(code, name, collegecode) \
            VALUES('{self.code}', '{self.name}', '{self.collegecode}')"
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls, course_code):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM courses WHERE code = %s"
            cursor.execute(sql, (course_code,))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting college: {e}")
            return False
        finally:
            cursor.close()

    @classmethod
    def update(cls, code, name, collegecode):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE courses
            SET name = %s,
                collegecode = %s
            WHERE code = %s
            """,
            (name, collegecode, code),
        )
        mysql.connection.commit()

    @classmethod
    def refer(cls):
        cursor = mysql.connection.cursor()

        sql = f"SELECT code FROM courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
