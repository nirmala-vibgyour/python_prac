import smtplib

# smtp: simple mail transfer protocol
# SMTP dictates how email messages should be formatted, encrypted, and relayed between mail servers, 
# and all the other details that the computer handles after the email is clicked Send.

# creates a session and pass the server location and port to use
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()

# 'auth', 'auth_cram_md5', 'auth_login', 'auth_plain', 'close', 'connect', 'data', 'debuglevel', 'default_port', 'docmd', 
# 'does_esmtp', 'ehlo', 'ehlo_msg', 'ehlo_or_helo_if_needed', 'ehlo_resp', 'expn', 'file', 'getreply', 'has_extn', 'helo', 
# 'helo_resp', 'help', 'login', 'mail', 'noop', 'putcmd', 'quit', 'rcpt', 'rset', 'send', 'send_message', 'sendmail', 
# 'set_debuglevel', 'sock', 'starttls', 'verify', 'vrfy'