import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from email.mime.base import MIMEBase
from email import encoders
#datos de sesion
global correo
def datos_sesion():
    os.system('cls')
    print("Datos de sesion")
    print("Ingrese su correo electronico")
    correo = input("Correo: ")
    print("Ingrese su contraseña")
    contraseña = getpass.getpass("Contraseña")
    return correo, contraseña
def adjuntar_archivo():
    os.system('cls')
    print("Adjuntar archivo")
    archivo_adjunto = input("Ingrese el nombre del archivo a adjuntar: ")
    with open(archivo_adjunto, "rb") as adjunto:
        contenido_adjunto = MIMEBase("application", "octet-stream")
        contenido_adjunto.set_payload(adjunto.read())
    encoders.encode_base64(contenido_adjunto)
    contenido_adjunto.add_header(
        "Content-Disposition",
        f"attachment; filename= {archivo_adjunto}",
    )
    return contenido_adjunto
def enviar_correo_con_archivo():

    #creo el mensaje
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = "Archivo adjunto"
    mensaje["From"] = correo
    mensaje["To"] = correo
    #creo el cuerpo del mensaje
    html = f"""\
    <html>
      <body>
        <p>Hola, <br>
           Le adjunto el archivo {contenido_adjunto}.<br>
           Saludos cordiales.
        </p>
      </body>
    </html>
    """
    #creo la parte html
    parte_html = MIMEText(html, "html")
    #adjunto la parte html al mensaje
    mensaje.attach(parte_html)
    #abro el archivo
    try:
        with open(archivo_adjunto, "rb") as attachment:
            #creo el tipo de archivo
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
    except:
        print(f"El archivo {archivo_adjunto} no existe")
        input("Presione una tecla para continuar...")
        return None
    #codifico el archivo
    encoders.encode_base64(part)
    #agrego el archivo al mensaje
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {archivo_adjunto}",
    )
    mensaje.attach(part)
    #creo el contexto
    context = ssl.create_default_context()
    #envio el correo
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(correo, contraseña)
        server.sendmail(correo, correo, mensaje.as_string())
        print("Correo enviado con exito")
    input("Presione una tecla para continuar...")
    return None
def enviar_correo():
    os.system('cls')
    print("Enviar correo")
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
    return None