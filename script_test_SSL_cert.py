from os import environ
from urllib.request import ssl, socket
import ssl

import datetime, smtplib

hostnames = ["www.impavi.de", "impavi.de"]
port = 443
context = ssl.create_default_context()
gmail_user = "daniel.muyshond@gmail.com"
gmail_app_password = environ.get("GMAIL_APP_PASSWORD")

for host in hostnames:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            cert = ssock.getpeercert()
            # print(cert)
            certExpires = datetime.datetime.strptime(
                cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
            )
            daysToExpiration = (certExpires - datetime.datetime.now()).days
            daysToExpiration = 1
            print(f"Days to expiration ({host}): ", daysToExpiration)
            if daysToExpiration == 7 or daysToExpiration == 1:
                sent_from = "Daniel Muyshond <daniel.muyshond@gmail.com>"
                to = ["daniel.muyshond@gmail.com"]
                valid_from = datetime.datetime.strptime(
                    cert["notBefore"], "%b %d %H:%M:%S %Y %Z"
                )
                valid_until = datetime.datetime.strptime(
                    cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
                )
                cert_issuer = cert["issuer"]
                cert_subject = cert["subject"]
                cert_version = cert["version"]
                serial_number = cert["serialNumber"]
                print(
                    "Valid from: ", valid_from,
                )
                print(
                    "Valid until: ", valid_until,
                )
                print("Issuer: ", cert_issuer)
                print("Subject: ", cert_subject)
                print("Version: ", cert_version)
                print("Serial Number: ", serial_number)
                subject = (
                    "Debian VPS 2022: SSL certificate for "
                    + host
                    + " expires in "
                    + str(daysToExpiration)
                    + " days."
                )
                print(subject)
                email_text = '''\\
                From: %s
                Subject: %s

                %s
                %s
                %s
                %s
                %s
                %s
                ''' % (
                    sent_from,
                    subject,
                    valid_from,
                    valid_until,
                    cert_issuer,
                    cert_subject,
                    cert_version,
                    serial_number,
                )

                print(email_text)
                try:
                    context = ssl.create_default_context()
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
                    server.ehlo()
                    server.login(gmail_user, gmail_app_password)
                    print(sent_from)

                    server.sendmail(sent_from, to, email_text)
                    server.close()

                    print("Email sent!")

                except Exception as e:
                    print("Something went wrong...", e)
