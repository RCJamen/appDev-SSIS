from app import mysql


class Colleges(object):
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO colleges(code, name) \
            VALUES('{self.code}', '{self.name}')"
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM colleges"
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
    def edit(cls, code):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM colleges WHERE code = {code}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def update(cls, code, name):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE colleges
            SET code = %s,
                name = %s
            WHERE code = %s
            """,
            (code, name),
        )
        mysql.connection.commit()

    @classmethod
    def refer(cls):
        cursor = mysql.connection.cursor()
        sql = f"SELECT code FROM colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
