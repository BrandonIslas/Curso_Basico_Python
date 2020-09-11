import smtplib

 #datos
username = input("pon tu correo:")
password = input("itroduce la clave de acceso a tu correo:")
destinatario  = input("correo de destino:")
msg = input("escribe el texto del mensaje:")

# Enviando el correo

#server = smtplib.SMTP('smtp.gmail.com:587') # con gmail
server = smtplib.SMTP('smtp-mail.outlook.com:587')
server.starttls()
server.login(username,password)
server.sendmail(username, destinatario, msg)
server.quit()

# server = smtplib.SMTP('smtp-mail.outlook.com:587') # con outlook
# server =  smtplib.SMTP('smtp.mail.yahoo.com:587') # con yahoo
# server =  smtplib.SMTP('smtp.mail.att.net:465') # con AT&T
# server =  smtplib.SMTP('smtp.comcast.net:465') # con COMCAST
# server =  smtplib.SMTP('smtp.verizon.net:465') # con verizon
# server =  smtplib.SMTP('smtp.mail.yahoo.com:587') # con yahoo
