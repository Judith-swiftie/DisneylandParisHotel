import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración de la cuenta de correo
mi_correo = "hoteles.disneyland.paris@gmail.com"
mi_contraseña = "lzekyvruhfhbbzid"

asunto = "Promoción Exclusiva en Disneyland París"
cuerpo_html = """
<html>
<head></head>
<body>
    <div style="border: 1px solid #ddd; padding: 20px; background-color: #ffffff;">
        <h3 style="color: #700029;">¡Descubre nuestras últimas novedades!</h3>
        <p>¡Hola! Aquí están nuestras últimas ofertas solo para ti.</p>

        <img src="https://drive.google.com/uc?export=view&id=1IzTsovpnpTsWUIiVVPK3aP0kc43ylUNC" width="80%" alt="Oferta especial" style="border-radius: 8px; margin-top: 10px; max-width: 600px;">

        <p style="margin-top: 20px;">Visítanos en nuestra página web para más información:</p>
        <a href="https://joyful-semifreddo-f8d800.netlify.app" style="color: #700029; text-decoration: none; font-weight: bold;">¡Explorar ahora!</a>

        <p style="font-size: 12px; color: #666; margin-top: 20px;">
            Para dejar de recibir nuestros correos, 
            <a href="https://joyful-semifreddo-f8d800.netlify.app/login" style="color: #d9534f;">haz clic aquí</a>.
        </p>
    </div>
</body>
</html>
"""

# Configuración del servidor SMTP y función de envío de correo


# Configuración del servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Función para enviar correo
def enviar_correo(destinatario):
    try:
        # Configurar el mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = mi_correo
        mensaje["To"] = destinatario
        mensaje["Subject"] = asunto
        mensaje.attach(MIMEText(cuerpo_html, "html"))

        # Conectar al servidor SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(mi_correo, mi_contraseña)
            server.sendmail(mi_correo, destinatario, mensaje.as_string())
            print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error al enviar correo a {destinatario}: {e}")

# Leer la base de datos y enviar correos a los usuarios que aceptaron recibir
def enviar_correos_promocionales(ruta_csv):
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            email = fila["email"]
            opt_in = int(fila["opt_in"])
            if opt_in == 1:  # Solo envía a quienes aceptaron
                enviar_correo(email)

# Llamar a la función con la ruta al archivo CSV
ruta_csv = "datos.csv"  # Cambia esto a la ruta de tu archivo CSV
enviar_correos_promocionales(ruta_csv)
 # type: ignore