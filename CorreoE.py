import smtplib 

#definir mensaje
message = 'Hola, necesito tu ayuda por favor'
subject ='ROSA ELENA RINCON'

message='Subject: {}\n\n{}'.format(subject,message)

server=smtplib.SMTP('smtp.gmail.com',587)#Definir objeto smtp, servidor que usaremos y el puerto
server.starttls()#indicar a nuestro progrma que haremos uso del protocolo tls
server.login('anamariamora0915@gmail.com', 'A2744763123')#auntenticarnos con nuestra cuenta de correo

server.sendmail('anamariamora0915@gmail.com', 'anamariamora09@hotmail.com', message)#enviar correo

server.quit()
print("El correo se ha enviado exitosamente")