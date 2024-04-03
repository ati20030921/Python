import flet as ft
import smtplib
from email.mime.text import MIMEText
from emailenvs import user


def automatic_email(to, subject, message):
    sender = user['account']
    password = user['password']
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    print(f"Email Sent!\nFrom: {sender}\nTo: {to}\nSubject: {subject}\n Message:\n{message}")
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(sender, password)
    s.sendmail(sender, to, msg.as_string())


def main(page: ft.Page):
    page.title = 'Email sender'

    def send_email(e):
        automatic_email(email_to.value, subject.value, message.value)

    email_to = ft.TextField(label='szt3daratt@vasvari.org')
    subject = ft.TextField(label='levél')
    message = ft.TextField(label='Egyél valamit')

    btn = ft.ElevatedButton(text='küldés',on_click=send_email)

    page.add(email_to,subject,message,btn)

ft.app(target=main)



    
    
