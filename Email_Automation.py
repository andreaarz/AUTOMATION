#  Código Python para enviar correos electrónicos personalizados

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP (en este caso, Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Credenciales del remitente
SENDER_EMAIL = "tuemail@gmail.com"
SENDER_PASSWORD = "tucontraseña"

# Lista de destinatarios y sus nombres
RECIPIENTS = [
    {"email": "destinatario1@example.com", "name": "John"},
    {"email": "destinatario2@example.com", "name": "Jane"},
    {"email": "destinatario3@example.com", "name": "Carlos"},
]

# Asunto del correo
SUBJECT = "¡Hola {name}! Este es tu recordatorio."

# Cuerpo del correo (puede ser un template con un campo de nombre dinámico)
BODY = """
Hola {name},

Este es un recordatorio importante para ti. No olvides revisar los detalles que te enviamos.

¡Saludos!
Tu equipo.
"""

# Función para enviar un correo a un destinatario
def send_email(recipient_name, recipient_email):
    # Crear el mensaje
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = recipient_email
    message["Subject"] = SUBJECT.format(name=recipient_name)

    # Personalizar el cuerpo del correo
    body = BODY.format(name=recipient_name)
    message.attach(MIMEText(body, "plain"))

    try:
        # Conectar al servidor SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Usar TLS para seguridad

        # Iniciar sesión en el servidor SMTP
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Enviar el correo
        server.sendmail(SENDER_EMAIL, recipient_email, message.as_string())
        print(f"Correo enviado a {recipient_email}")
    except Exception as e:
        print(f"Error al enviar correo a {recipient_email}: {e}")
    finally:
        server.quit()

# Enviar correos a todos los destinatarios
for recipient in RECIPIENTS:
    send_email(recipient["name"], recipient["email"])

""" Explicacion:
Configuración SMTP:

SMTP_SERVER y SMTP_PORT: Especifican el servidor y el puerto del servidor SMTP. En este caso, estamos utilizando Gmail (aunque puedes cambiar esto para otros proveedores).
SENDER_EMAIL y SENDER_PASSWORD: Son las credenciales de tu cuenta de correo de Gmail que usarás para enviar los correos. Recuerda no compartir estos datos y considerar opciones más seguras como el uso de OAuth2.
Lista de destinatarios:

RECIPIENTS: Esta lista contiene los correos electrónicos y los nombres de los destinatarios. Puedes agregar más destinatarios según sea necesario.
Correo personalizado:

El asunto y el cuerpo del correo están diseñados para ser personalizados con el nombre de cada destinatario. Se usa {name} como un marcador que se reemplaza con el nombre de cada persona.
Función send_email:

Esta función maneja el envío de un correo electrónico a un destinatario específico. Usa MIMEText y MIMEMultipart para estructurar el contenido del correo (en este caso, un correo de texto sin formato).
La función se conecta al servidor SMTP y envía el correo. Si ocurre un error, se captura y se imprime.
Envío a todos los destinatarios:

En la última parte, se recorre la lista de destinatarios y se llama a send_email para enviar el correo a cada uno.
Seguridad:
Contraseña: Si estás usando Gmail, considera usar contraseñas de aplicación si tienes habilitada la verificación en dos pasos. En vez de tu contraseña habitual, generarías una contraseña única para este script. No es recomendable poner tu contraseña directamente en el código.

"""

