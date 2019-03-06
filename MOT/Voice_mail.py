import os
import datetime
import smtplib
import mimetypes
import imghdr
import sndhdr

from argparse import ArgumentParser
from email.message import EmailMessage
from email.policy import SMTP

def create_message(from_addr, to_addr, subject, body, attach_file):
    #メッセージをつくる
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.set_content(body)
    #添付ファイルを作成する。
    file = open(attach_file['path'],'rb')
    file_read = file.read()
    #msg.add_attachment(file_read, maintype='image',subtype=imghdr.what(None,file_read),filename=attach_file['name'])
    msg.add_attachment(file_read, maintype='audio',subtype=sndhdr.what(file_read),filename=attach_file['name'])
    file.close()

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
subject = "音声ファイルを添附します。"
body = "音声ファイルを添附します。確認お願いします。\n"
mine={'type':'text','subtype':'comma-separated-values'}
    #メール送信の関数の実行
attach_file={'name':'your_boicefile','path':'your_path'}

msg = create_message(from_addr, to_addr, subject, body, attach_file)
sendGmail(from_addr, to_addr, msg)

#GPIO.cleanup() # GPIO初期化
