import smtplib

# Establish a connection to the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 465)
server.starttls()
print('Server started...')

# Login to your Gmail account
try:
    server.login('guguloth.rajashekhar@talentpace.com', 'talentpace@123')
    print('Login successful...')

    # Send an email
    server.sendmail(
        'guguloth.rajashekhar@talentpace.com', 
        'shekarnaik826@gmail.com', 
        'Subject: Test Mail\n\nHello thammudu.....'
    )
    print('Mail sent...')
except smtplib.SMTPAuthenticationError as e:
    print('Failed to login:', e)
finally:
    # Close the server connection
    server.quit()
