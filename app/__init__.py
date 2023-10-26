from flask import Flask, render_template
from flask_mysql_connector import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
    )

    mysql.init_app(app)
    CSRFProtect(app)

    # Blueprints
    from .controller.students import student
    from .controller.courses import course
    from .controller.colleges import college

    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)

    return app
