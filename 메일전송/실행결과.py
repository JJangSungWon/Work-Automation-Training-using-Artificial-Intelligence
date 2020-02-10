#앱 비밀번호를 넣지 않은 상태라 바로 돌리면 돌아가지 않습니다.
#앱 비밀번호 및 메일 주소를 변경 후 실행하면 됩니다.
#앱 비밀번호는 계정의 비밀번호가 아닙니다!

import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

#앱 비밀번호는 계정의 비밀번호가 아니다!
'''
step1 
- gmail로그인 후 우측 상단의 톱니바퀴 모양의 아이콘을 눌러 설정이동
- 상단 바에 전달 및 POP/IMAP 선택
- IMAP 사용으로 바꾸고 저장

step2 
https://myaccount.google.com/security 접속하여 2단계 인증을 진행한 후 앱 비밀번호 설정
앱 선택 - 메일, 기기 선택 - Windows 컴퓨터 
'''

s.login('dnjs2113@gmail.com', '비밀번호')

msg = MIMEText('내용 : 본문내용 테스트입니다.')
msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'

s.sendmail("dnjs2113@gmail.com", "testtesttestsmtplib@gmail.com", msg.as_string()) #발신 메일, 수신 메일

s.quit()
