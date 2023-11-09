import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')
# DB와 파이썬파일 사이의 연결통로가 생성

sql = "INSERT INTO member VALUES('blackcat','12345','이순신','010-8899-9988','경기도 안산시',61)"
# sql문 생성하여 문자열로 저장

cur = conn.cursor() # 커서 생성
cur.execute(sql) # SQL문 실행

cur.close()
conn.commit() # insert, delete, update sql문을 사용한 경우에는 반드시 commit 해줘야 함!
conn.close()

