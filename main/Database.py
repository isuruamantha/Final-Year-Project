import hashlib
import os

from flask import Flask
from flaskext.mysql import MySQL
from pymysql import Error

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'saransha'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
conn.autocommit(True)


# Check the login credentials
def login_user(userName, userPassword):
    """
    :param userName: Entered User name
    :param userPassword: Entered userpassword without hasing
    :return: whether the request is success or not
    """
    return_value = ""
    cur = conn.cursor()
    password = hashlib.md5(userPassword.encode())
    cur.execute("""SELECT * FROM user where userName = (%s)""", (userName))

    for row in cur.fetchall():
        if (row[2] == password.hexdigest()):
            return_value = "success"
        else:
            return_value = "fail"
    cur.close()

    return return_value


# Register the user
def user_signup(userName, userPassword, userEmail):
    """
    :param userName: Entered username
    :param userPassword: Entered userpassword
    :param userEmail: entered user email
    :return: success state of the request
    """
    cur = conn.cursor()

    password = hashlib.md5(userPassword.encode())

    query = "INSERT INTO user(userName,userPassword, userEmail) " \
            "VALUES(%s,%s,%s)"
    args = (userName, password.hexdigest(), userEmail)

    cur.execute(query, args)
    cur.close()

    return "Success"
