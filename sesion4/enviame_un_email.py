
import smtplib
import ssl
import sys
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
import getpass

# Comprobar que se ha pasado el mensaje
if len(sys.argv) < 2:
    print("Uso: python3 enviame_un_email.py 'mensaje'")
    sys.exit(1)

# Configuración SMTP
server = "smtp.gmail.com"
port = 587

# Direcciones
fromaddr = input("Usuario (correo Gmail): ")
password = getpass.getpass("Contraseña de aplicación: ")
toaddr = input("Destinatario (correo Uniovi): ")

# Datos del mensaje
subject = "Correo de prueba"
texto = " ".join(sys.argv[1:])

# Construir el mensaje
mensaje = EmailMessage()
mensaje["From"] = fromaddr
mensaje["To"] = toaddr
mensaje["Subject"] = subject
mensaje["Date"] = formatdate(localtime=True)
mensaje["Message-ID"] = make_msgid()
mensaje.set_content(texto)

# Conexión segura
context = ssl.create_default_context()
s = smtplib.SMTP(server, port)

try:
    s.ehlo()
    s.starttls(context=context)
    s.ehlo()

    # Autenticación
    s.login(fromaddr, password)

    # Enviar correo
    s.sendmail(fromaddr, [toaddr], mensaje.as_bytes())

    print("Correo enviado correctamente")

finally:
    s.quit()
