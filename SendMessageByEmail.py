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
        txt["To"] = "Hola@gmail.com";
        
        #txt["Subject"] = "Report"+  str(datetime.datetime.now().date());
        #txt.attach(MIMEText(message,"plain"));

        # Conexion al server de Google
        server = smtplib.SMTP('smtp.gmail.com: 587');
        # Inicia Conexion
        server.starttls();
        # Inicia sesión [User : emailPass] = google.com
        server.login(txt["From"], emailPass);
        server.quit();
        # En caso de Envio Exitoso , retorna un True
        return True;
    except:
        return False;


