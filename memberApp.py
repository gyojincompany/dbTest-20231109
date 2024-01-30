# 회원 가입 프로그램

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

form_class = uic.loadUiType("ui/member3.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원가입 프로그램")

        self.idcheck_btn.clicked.connect(self.idCheck)
        self.join_btn.clicked.connect(self.memberJoin)
        self.login_btn.clicked.connect(self.memberLogin)
        self.reset_btn.clicked.connect(self.reset)  # 조회 버튼 클릭시 reset 함수 호출

        self.reset_btn_2.clicked.connect(self.reset2)

        self.search_btn.clicked.connect(self.db_search)  # 조회 버튼 클릭시 db_search 함수 호출
        self.modify_btn.clicked.connect(self.db_modify)  # 조회 버튼 클릭시 db_modify 함수 호출
        self.reset_btn_3.clicked.connect(self.reset3)  # 조회 버튼 클릭시 reset 함수 호출

    
    def idCheck(self):
        memberid = self.memberid_edit.text()  # 회원아이디로 입력된 아이디 텍스트 가져오기

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM member WHERE memberid='{memberid}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        result = cur.fetchone()
        # print(result)
        
        if result == None: # 회원가입가능
            QMessageBox.warning(self, '가입가능', '입력하신 아이디는 가입 가능한 아이디입니다. 계속해서 가입 진행하세요.')
            self.reset_btn.clicked.connect(self.reset)
        else:
            QMessageBox.warning(self, '가입불가', '입력하신 아이디는 이미 존재하는 아이디입니다. 다른 아이디를 입력하세요.')

        cur.close()
        conn.close()

    def memberJoin(self):

        memberid = self.memberid_edit.text()  # 회원아이디로 입력된 아이디 텍스트 가져오기
        memberpw = self.memberpw_edit.text()  # 회원비밀번호 텍스트 가져오기
        name = self.name_edit.text()  # 회원비밀번호 텍스트 가져오기
        phone = self.phone_edit.text()  # 회원전화번호 텍스트 가져오기
        address = self.address_edit.text()  # 회원주소 텍스트 가져오기
        age = self.age_edit.text()  # 회원나이 텍스트 가져오기
        print(memberid)
        print(memberpw)
        print(name)
        print(phone)
        print(age)

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"INSERT INTO member VALUES ('{memberid}', '{memberpw}', '{name}', '{phone}', '{address}', {age})"

        cur = conn.cursor()  # 커서 생성
        result = cur.execute(sql)  # SQL문 실행

        print(result)

        if result == 1:
            QMessageBox.warning(self, '가입성공!', '입력하신 회원정보로 회원가입이 성공하였습니다.')
            self.reset()
        else:
            QMessageBox.warning(self, '가입실패!', '입력하신 회원정보로 회원가입이 실패하였습니다. 다시확인해 주세요.')

        cur.close()
        conn.commit()
        conn.close()


    def memberLogin(self):
        loginid = self.loginid_edit.text()  # 로그인아이디로 입력된 아이디 텍스트 가져오기
        loginpw = self.loginpw_edit.text()  # 로그인비밀번호 텍스트 가져오기

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM member WHERE memberid='{loginid}' and memberpw='{loginpw}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        result = cur.fetchone()
        print(result)

        if result == None:
            self.logintext_label.setText('로그인 실패. 아이디 또는 비밀번호를 확인하세요.')
        else:
            self.logintext_label.setText('로그인 성공!')
            self.reset2()


        cur.close()
        conn.close()

    def db_search(self):
        memberid = self.memberid_edit_2.text() # 회원아이디로 입력된 아이디 텍스트 가져오기

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM member WHERE memberid='{memberid}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행

        result = cur.fetchone()

        cur.close()
        conn.close()
        # print(result)
        if result != None:
            self.memberpw_edit_2.setText(result[1])
            self.name_edit_2.setText(result[2])
            self.phone_edit_2.setText(result[3])
            self.address_edit_2.setText(result[4])
            self.age_edit_2.setText(str(result[5]))
            # age(result[5])가 정수이므로 문자열로 변환
        else:
            self.memberpw_edit_2.setText('회원정보없음')
            self.name_edit_2.setText('회원정보없음')
            self.phone_edit_2.setText('회원정보없음')
            self.address_edit_2.setText('회원정보없음')
            self.age_edit_2.setText('회원정보없음')

    def db_modify(self):
        memberid = self.memberid_edit_2.text() # 회원아이디로 입력된 아이디 텍스트 가져오기
        memberpw = self.memberpw_edit_2.text() # 회원비밀번호 텍스트 가져오기
        name = self.name_edit_2.text() # 회원비밀번호 텍스트 가져오기
        phone = self.phone_edit_2.text() # 회원전화번호 텍스트 가져오기
        address = self.address_edit_2.text() # 회원주소 텍스트 가져오기
        age = self.age_edit_2.text() # 회원나이 텍스트 가져오기

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"UPDATE member SET memberpw='{memberpw}',name='{name}',phone='{phone}',address='{address}',memberage={age} WHERE memberid='{memberid}'"

        cur = conn.cursor()  # 커서 생성
        result = cur.execute(sql)  # SQL문 실행

        if result == 1:
            QMessageBox.warning(self, '회원정보 수정성공!', '입력하신 회원정보로 회원정보 수정이 성공하였습니다.')
            self.reset()
        else:
            QMessageBox.warning(self, '회원정보 수정실패!', '입력하신 회원정보로 회원정보 수정이 실패하였습니다. 다시확인해 주세요.')

        cur.close()
        conn.commit()
        conn.close()

        self.db_search() # 다시 데이터 갱신

    def reset(self):
        self.memberid_edit.clear()
        self.memberpw_edit.clear()
        self.name_edit.clear()
        self.phone_edit.clear()
        self.address_edit.clear()
        self.age_edit.clear()

    def reset2(self):
        self.loginid_edit.clear()
        self.loginpw_edit.clear()

    def reset3(self):
        self.memberid_edit_2.clear()
        self.memberpw_edit_2.clear()
        self.name_edit_2.clear()
        self.phone_edit_2.clear()
        self.address_edit_2.clear()
        self.age_edit_2.clear()



if __name__== '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())