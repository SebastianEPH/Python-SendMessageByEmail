# Importar SendGmail()
from SendMessageByEmail import *

# Variables 
message   = "";         # message que se enviará
emailUser = "";         # Email envía - Name        # CorreoQueEnviaraElMensaje@gmail.com
emailPass = "";         # Email envía - emailPass   # Contraseña
emailTo   = "";         # Email receptor            # CorreoQueRecibaElMensaje@hotmail.com // @gmail.com // @t.hotmail.cn

# Nota importante
# El correo que envíará el mensaje debe estar habilitado 
# "Aplicaciones menos seguras"
# Tutorial de como activarlo o desactivarlo
# Entrar a este link-.. (link no habilitado por ahora), puedes buscar por google


# bucle infinito para enviar el correo 
while True:
    print("Resultado de Envío: "+str(SendGmail(emailUser,emailPass,emailTo,message)));

