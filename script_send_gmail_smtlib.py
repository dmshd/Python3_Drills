from os import environ
from urllib.request import ssl, socket


import smtplib
from email.mime.text import MIMEText

# GMail auth details
gmail_user = environ.get("GMAIL_USER")
gmail_app_password = environ.get("GMAIL_APP_PASSWORD")
sender = environ.get("GMAIL_SENDER")
receiver = gmail_user

# Create SMTP session
with smtplib.SMTP("smtp.gmail.com", 587) as s:

    # Start TLS for security
    s.starttls()

    # Authentification
    s.login(gmail_user, gmail_app_password)

    # Define the message
    email = MIMEText("This is an email sent with Python")
    email["Subject"] = "Hello, here is your mail sent with Python"
    email["From"] = gmail_user
    email["To"] = gmail_user
    # breakpoint()
    s.sendmail(sender, receiver, email.as_string())
    """
    as_string() is used to convert the MIMEText object (msg)
    into a string representation of the email message. This
    is necessary because the sendmail() function of the smtplib
    module, which is used to send the email, expects a string
    argument representing the message to be sent.

    The as_string() method of the MIMEText object returns a
    string representation of the message that includes the
    headers (such as the subject and the sender and recipient
    addresses) and the message body. This string can then be
    passed to the sendmail() function to send the email.
    """


# def send_notification(host):
#     import smtplib

#     gmail_user = "daniel.muyshond@gmail.com"
#     gmail_app_password = environ.get('GMAIL_APP_PASSWORD')
#     sent_from = gmail_user
#     to = ["daniel.muyshond@gmail.com"]
#     subject = "OMG Super Important Message"
#     body = "Hey, what's up?\n\n- You"

#     email_text = """\
#     From: %s
#     To: %s
#     Subject: %s

#     %s
#     """ % (sent_from, ", ".join(to), subject, body)

#     try:
#         ssl_context = ssl.create_default_context()
#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         server.ehlo()
#         server.login(gmail_user, gmail_app_password)
#         server.sendmail(sent_from, to, email_text)
#         server.close()

#         print('Email sent!')

#     except Exception as e:
#         print('Something went wrong...', e)

# if __name__ == '__main__':
#     send_notification('impavi.de')
