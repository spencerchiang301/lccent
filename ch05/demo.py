import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='nicole',
        database='training'
    )
    cursor = conn.cursor()
    cursor.execute('select * from students')
    results = cursor.fetchall()

    print("all data")
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print("database erorr: {}".format(err))