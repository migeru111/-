import os
import datetime
import smtplib
import mimetypes
import imghdr
import sndhdr

from argparse import ArgumentParser
from email.message import EmailMessage
from email.policy import SMTP

def create_message(from_addr, to_addr, subject, body):
    #メッセージをつくる
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.set_content(body)
    #添付ファイルを作成する。
    #file = open(attach_file['path'],'rb')
    #file_read = file.read()
    #msg.add_attachment(file_read, maintype='image',subtype=imghdr.what(None,file_read),filename=attach_file['name'])
    #msg.add_attachment(file_read, maintype='audio',subtype=sndhdr.what(None,file_read),filename=attach_file['name'])
    #file.close()

    return msg

def sendGmail(from_addr, to_addr, msg):
    #メールを送る。
    #print(msg)
    smtp = smtplib.SMTP_SSL(host, port)
    smtp.ehlo()
    smtp.login(username, password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    smtp.quit()

#if __name__ == '__main__':

    #Gメールのパスワードやポートの設定
host, port = 'smtp.gmail.com', 465
username, password = 'Gmail_username', 'Gmail_pass'

    #送信用データの設定
from_addr ="from_mailaddres"
to_addr = "to_mailaddres"
subject = "調子は快調です。"
body = "調子は快調です。今日も元気に頑張ります！！\n"
mine={'type':'text','subtype':'comma-separated-values'}
    #メール送信の関数の実行
#attach_file={'name':'aaa.wav','path':'/home/pi/Mot/aaa.wav'}

msg = create_message(from_addr, to_addr, subject, body)
sendGmail(from_addr, to_addr, msg)

#GPIO.cleanup() # GPIO初期化
