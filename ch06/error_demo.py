import mysql.connector
# 引用 logging
import logging

# 配置logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('./mysql.log'),
                              logging.StreamHandler()])

try:
    logger = logging.getLogger("error_demo")
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='nicole',
        database='traning'
    )
    cursor = conn.cursor()
    cursor.execute('select * from students')
    results = cursor.fetchall()

    print("all data")
    for row in results:
        print(row)

except mysql.connector.Error as err:

    print("database erorr: {}".format(err))