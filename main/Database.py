import datetime
import hashlib
import os
import time
from flask import Flask, jsonify, Response, json
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

    variable = []

    for row in cur.fetchall():
        if (row[2] == password.hexdigest()):
            requestStatus = "success"
            variable.append(requestStatus)
            variable.append(userName)
            variable.append(row[0])
        else:
            requestStatuss = "fail"
            variable.append(requestStatuss)

    cur.close()

    if (len(variable) == 0):
        requestStatuss = "fail"
        variable.append(requestStatuss)

    response = Response(
        response=json.dumps(variable),
        status=200,
        mimetype='application/json'
    )
    return response


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


# To save the generated summary in the database
def save_summary(userId, summary):
    """
    :param userId: Id of the user
    :param summary: Desired summary to be saved
    :return: status of the request
    """
    cur = conn.cursor()
    date = time.time()
    timestamp = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp)
    query = "INSERT INTO summary(userId, summary, createdDate) " \
            "VALUES(%s,%s,%s)"
    args = (userId, summary, timestamp)

    cur.execute(query, args)
    cur.close()
    return "Success"


# Return the user history
def history(userId):
    """
    :param userId:
    :return: Return the history
    """
    return_value = ""
    cur = conn.cursor()
    cur.execute("""SELECT * FROM summary where userId = (%s)""", (userId))

    topList = []
    for row in cur.fetchall():
        tmpDict1 = {}
        tmpDict1["key"] = "1"
        tmpDict1["value"] = row[2]
        tmpDict1["created date"] = row[3].replace(tzinfo=None)
        topList.append(tmpDict1)

    cur.close()

    return jsonify(topList)
