
import  smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender_email = "aj2215singh@gmail.com"
rec_email = "14.akansha.chhattri@gmail.com"
password = "dlbk***********ksjaix"
message = "Face detacted, alert"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login")
server.sendmail(sender_email, rec_email, message)
print("Email send" , rec_email)



with open('', 'file_open_mode') as variable_name:
    variable_for_storing_image_data = variable_name.read()
