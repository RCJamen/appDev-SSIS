from flask import Flask, render_template
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    #Blueprints
    # from .views.students import student
    # from .views.courses import course
    # from .views.colleges import college
    # app.register_blueprint(student)
    # app.register_blueprint(course)
    # app.register_blueprint(college)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('students.html')

    return app