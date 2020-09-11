#!/usr/bin/python
#-*- coding: utf-8 -*-

#Enviar correo Gmail con python

import smtplib

remitente = 'brandon.esocm.98@gmail.com'
destinatario = 'brandon98642@gmail.com'
msg='Correo enviadi utilizando Python + smtplib '

#Datos
username ='brandon.esocm.98@gmail.com'
password ='50502720'

#Enviando el Correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(remitente,destinatario,msg)
server.quit()
