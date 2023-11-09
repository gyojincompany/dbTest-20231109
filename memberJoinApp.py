# 회원 가입 프로그램

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

form_class = uic.loadUiType("ui/join.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원가입 프로그램")

        self.idcheck_btn.clicked.connect(self.idCheck)
    
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
        else:
            QMessageBox.warning(self, '가입불가', '입력하신 아이디는 이미 존재하는 아이디입니다. 다른 아이디를 입력하세요.')

        cur.close()
        conn.close()


if __name__== '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())