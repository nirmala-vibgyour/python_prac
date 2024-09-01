import smtplib

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration for Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 465  # SSL/TLS port for Gmail
username = 'your_email@gmail.com'
password = 'your_password'
from_email = 'your_email@gmail.com'
to_email = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email sent from Python using Gmail with SSL/TLS.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Create an SMTP_SSL connection
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(username, password)  # Log in to the server
        server.sendmail(from_email, to_email, msg.as_string())  # Send the email
    print('Email sent successfully')
except smtplib.SMTPAuthenticationError as e:
    print(f'SMTPAuthenticationError: Authentication failed: {e}')
except smtplib.SMTPException as e:
    print(f'SMTPException: An error occurred while sending the email: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
