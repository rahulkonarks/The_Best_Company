import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    with open("/home/konarkguatam/Email.txt", 'r') as file:
        email = file.read()
        email = email.strip("\n")

    with open("/home/konarkguatam/App_Password.txt", 'r') as file:
        password = file.read()
        password = password.strip("\n")

    receiver = email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, receiver, message)
