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
    def delete(cls, code):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM colleges WHERE code = %s"
            cursor.execute(sql, (code,))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting college: {e}")
            return False
        finally:
            cursor.close()

    @classmethod
    def edit(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM courses WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def update(cls, id, code, name, collegecode):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE courses
            SET code = %s,
                name = %s,
                collegecode = %s
            WHERE id = %s
            """,
            (code, name, collegecode, id),
        )
        mysql.connection.commit()

    @classmethod
    def refer(cls):
        cursor = mysql.connection.cursor()

        sql = f"SELECT code FROM courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
