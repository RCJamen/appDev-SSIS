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
    def exists(cls, code):
        cursor = mysql.connection.cursor()
        check_sql = "SELECT code FROM colleges WHERE code = %s"
        cursor.execute(check_sql, (code,))
        existing_student = cursor.fetchone()
        return existing_student is not None

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls, college_code):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM colleges WHERE code = %s"
            cursor.execute(sql, (college_code,))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting college: {e}")
            return False
        finally:
            cursor.close()

    @classmethod
    def update(cls, code, name):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE colleges
            SET name = %s
            WHERE code = %s
            """,
            (name, code),
        )
        mysql.connection.commit()

    @classmethod
    def refer(cls):
        cursor = mysql.connection.cursor()
        sql = f"SELECT code FROM colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def search(cls, info):
        print(info)
        cursor = mysql.connection.cursor()
        keywords = info.split()
        conditions = []
        for keyword in keywords:
            conditions.append(f"name LIKE '%{keyword}%'")
        conditions_sql = " OR ".join(conditions)
        sql = f"SELECT * FROM colleges WHERE code = '{info}' OR ({conditions_sql})"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
