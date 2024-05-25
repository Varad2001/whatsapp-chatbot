import os
import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
from email.header import decode_header

from src.config import EMAIL, PASSWORD,IMAP_SERVER, IMAP_PORT , SMTP_SERVER , SMTP_PORT 


def send_email(receiver_email, body, subject):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(EMAIL, receiver_email, text)
        print('Email sent successfully')
        status = "success"

    except Exception as e:
        print(f'Failed to send email: {e}')
        status = f"failure:{str(e)}"

    finally:
        server.quit()
    return status



def fetch_last_emails(num):
    # Connect to the server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL, PASSWORD)
    
    # Select the mailbox you want to check
    mail.select("inbox")

    # Search for all emails in the inbox
    status, messages = mail.search(None, "ALL")

    if status == "OK":
        # Convert messages to a list of email IDs
        email_ids = messages[0].split()

        # Fetch the last 10 emails (or fewer if there are not enough emails)
        for num in email_ids[-num:]:
            status, data = mail.fetch(num, "(RFC822)")
            if status == "OK":
                msg = email.message_from_bytes(data[0][1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                from_ = msg.get("From")
                print(f"Subject: {subject}")
                print(f"From: {from_}")
                #print(f"Body:\n{msg.keys()}")
                print()

    mail.logout()

if __name__ == "__main__":
    #fetch_last_emails(2)
    send_email(receiver_email="varadkhonde@gmail.com")
