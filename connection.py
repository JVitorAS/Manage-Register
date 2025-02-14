import mysql.connector
def get_connection():
    host = '127.0.0.1'
    user = 'root'
    password = ''
    database = 'COMPANYDB'
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )