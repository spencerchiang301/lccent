import mysql.connector

try:
    conn = mysql.connector.connect(
        host='172.16.1.112',
        port=3306,
        user='root',
        password='nicole',
        database='training'
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM person")
    results = cursor.fetchall()

    print("所有資料：")
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print("資料庫錯誤：", err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()