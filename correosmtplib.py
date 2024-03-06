import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
#datos de sesion
global correo
def datos_sesion():
    os.system('cls')
    print("Datos de sesion")
    print("Ingrese su correo electronico")
    correo = input("Correo: ")
    print("Ingrese su contraseña")
    contraseña = getpass.getpass("Contraseña: ")
    return correo, contraseña
destinatario= input("Ingrese el correo del destinatario: ")
asunto = input("Ingrese el asunto: ")
#creo el mensaje
mensaje = MIMEMultipart("alternative")
mensaje["Subject"] = asunto
mensaje["From"] = correo
mensaje["To"] = destinatario
#creo el cuerpo del mensaje
html = f"""\
<html>
  <body>
    <p>Hola, {1} <br>
       Le informamos que ha sido asignado al grupo de trabajo {1}.<br>
       ya en clase se le informara sobre las actividades a realizar.<br>
       Saludos cordiales.
    </p>
  </body>
</html>
"""
#creo la parte html
parte_html = MIMEText(html, "html")
#adjunto la parte html al mensaje
mensaje.attach(parte_html)
#creo el contexto
context = ssl.create_default_context()
#envio el correo
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(correo, contraseña)
    server.sendmail(correo, destinatario, mensaje.as_string())
    print("Correo enviado con exito")
input("Presione una tecla para continuar...")



