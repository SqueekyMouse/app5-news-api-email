import smtplib
import ssl
import os

def send_email(message,sub=''):
    host='smtp.gmail.com'
    port=465
    username='appuser565@gmail.com'
    password=os.getenv('APP_M_PASSWORD')
    receiver='appuser565@gmail.com'
    context=ssl.create_default_context()
    
    # creating raw mail due to err as msg has non ascii chars
    # UnicodeEncodeError: 'ascii' codec can't encode character
    # raw_msg=f'From: {username}\r\nTo: {receiver}\r\nSubject: {sub}\r\n{message}'
    # raw_msg=f'Subject: {sub}\r\n{message}'
    
    with smtplib.SMTP_SSL(host=host,port=port,context=context) as server:
        server.login(user=username,password=password)
        # server.sendmail(from_addr=username,to_addrs=receiver,
                        # msg=raw_msg.encode(encoding='utf-8'))
        server.sendmail(from_addr=username,to_addrs=receiver,
                        msg=message)

