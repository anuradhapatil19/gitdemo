# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("www.jaypalpawar325@gmail.com", "admin@123")

# message to be sent
message = "otp testing"

# sending the mail
s.sendmail("www.jaypalpawar325@gmail.com", "pawarjaypal325@gmail.com", message)

# terminating the session
s.quit()

print("email sent...!")
