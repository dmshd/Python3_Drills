# I want you to act as a software developer. I will provide some code and it will be your job to come up with suggesti
# ons of improvements. My first request is what can I do better about this :

import smtplib, ssl
from email.message import EmailMessage
import socket
import datetime
from os import environ

SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "daniel.muyshond@gmail.com"
RECEIVER_EMAIL = "daniel.muyshond@gmail.com"
password = environ.get("GMAIL_APP_PASSWORD")
if password is None:
    print("Error: GMAIL_APP_PASSWORD environment variable is not set")
    exit(1)

# Create SSL context with cert verif enabled
context = ssl.create_default_context()
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED

# Deine the hostname
host = "impavi.de"
port = 443

# Create a new email message
mail = EmailMessage()

# Connect to the server and get the SSL certificate
with socket.create_connection((host, port)) as sock:
    with context.wrap_socket(sock, server_hostname=host) as ssock:

        cert = ssock.getpeercert()

        # Parse the certificate expiration date
        certExpires = datetime.datetime.strptime(
            cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
        )

        # Calculate the number of days until the cert expires
        days_to_expiration = (certExpires - datetime.datetime.now()).days
        print(f"Days to expiration ({host}): ", days_to_expiration)
        days_to_expiration = 1
        # Check if the certificate is due to expire in 7 or 1 day
        if days_to_expiration == 7 or days_to_expiration == 1:

            # Parse the certificate validity dates
            valid_from = datetime.datetime.strptime(
                cert["notBefore"], "%b %d %H:%M:%S %Y %Z"
            )
            valid_until = datetime.datetime.strptime(
                cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
            )

            # Get the cert info
            cert_issuer = cert["issuer"]
            cert_subject = cert["subject"]
            cert_version = cert["version"]
            serial_number = cert["serialNumber"]

            # Set the email body
            content = (
                "Hello Daniel,\n\nThe impavi.de SSL certificates needs your attenion.\n\nKind regards,\nYou\n\n%s\n%s\n%s\n%s\n%s\n%s"
                % (
                    valid_from,
                    valid_until,
                    cert_issuer,
                    cert_subject,
                    cert_version,
                    serial_number,
                )
            )
            mail.set_content(content)

            # Set the email subject
            mail[
                "Subject"
            ] = f"Debian VPS 2022: SSL certificate for {host} expires in {days_to_expiration} days"
            mail["From"] = SENDER_EMAIL
            mail["To"] = RECEIVER_EMAIL
            try:
                with smtplib.SMTP_SSL(
                    SMTP_SERVER, 465, context=context
                ) as server:  # 465 for SSL
                    server.login(SENDER_EMAIL, password)
                    server.send_message(
                        mail, from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL
                    )
                    server.close()
                    print("Email sent!")
            except (smtplib.SMTPException, ssl.SSLError) as e:
                print("Something went wrong...", e)
    ssock.close()
sock.close()
