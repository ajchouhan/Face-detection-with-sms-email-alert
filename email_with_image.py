import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "aj2215singh@gmail.com"
Reciever_Email = "14.akansha.chhattri@gmail.com"
Password = "dlb*******************ksjaix"

newMessage = EmailMessage()                         
newMessage['Subject'] = "Check out the new logo" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('security alert face detecd. Image attached!') 

with open('crop.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage) 
