
import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()


s.login("sender mail", "sender password")


message = "otp testing"


s.sendmail("sender_mail", "receiver_mail", message)

s.quit()

print("email sent...!")
