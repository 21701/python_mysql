import mysql.connector

try :
    # 1. DB 에 연결
    connection = mysql.connector.connect(
        host = 'yh-db.c7guy9txcxzu.ap-northeast-2.rds.amazonaws.com',
        database = 'streamlit_db',
        user = 'python_user',
        password = '4444'
    )

    name = '미애'
    id = 6

    # date = '2021-12-15'

    # 2. 쿼리문 만들고
    query = '''update test
                set name = %s
                where id = %s ;'''
    # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭
    # 써준다.
    
    record = (name,id)
    

    # 3. 커넥션으로부터 커서를 가져온다.
    cursor = connection.cursor()

    # 4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.execute(query,record)

    # 5. 커넥션을 커밋한다. => 디비에 영구적으로 반영하라는 뜻
    connection.commit()

except mysql.connector.Error as e :
    print('Error', e)

finally :
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')