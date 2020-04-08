# Importamos librería, enviar Gmail
from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;
import smtplib;
import datetime;


def SendGmail(emailUser,emailPass,emailTo,message):
    txt = MIMEMultipart();
    # Enviar Desde
    txt["From"] = emailUser;
    # a
    txt["To"] = emailTo;
    txt["Subject"] = "Report"+  str(datetime.datetime.now().date());
    txt.attach(MIMEText(message,"plain"));
    try:
        # Conexion al server de Google
        server = smtplib.SMTP('smtp.gmail.com: 587');
        # Inicia Conexion
        server.starttls();
        # Inicia sesión [User : emailPass] = google.com
        server.login(txt["From"], emailPass);
        # Envía Mensaje 
        server.sendmail(txt["From"], txt["To"], txt.as_string());
        # Cierra Conexión al servidor
        server.quit();
        # En caso de Envio Exitoso , retorna un True
        return True;
    except:
        return False;

def TestSend (emailUser,emailPass):
    try:
        txt = MIMEMultipart();
        # Enviar Desde
        txt["From"] = emailUser;
        # a
        txt["To"] = "hola@gmail.com";   # Correo de la persona a la cual se le enviará el mensaje 
        txt["Subject"] = "Texto Encabezado"+  str(datetime.datetime.now().now());
        txt.attach(MIMEText(" Escribe el texto que quieres enviar aquí  ","plain"));
        # Conexion al server de Google
        server = smtplib.SMTP('smtp.gmail.com: 587');
        # Inicia Conexion
        server.starttls();
        # Inicia sesión [User : emailPass] = google.com
        server.login(txt["From"], emailPass);
        # Envía Mensaje 
        server.sendmail(txt["From"], txt["To"], txt.as_string());
        # Cierra Conexión al servidor
        server.quit();
        # En caso de Envio Exitoso , retorna un True
        print("El Correo se envió correctamente");
        return True;
    except:
        print("Error de envio");
        return False;


