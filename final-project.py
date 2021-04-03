#Module untuk melakukan pengiriman email
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Memasukkan alamat email pengirim, penerima, subjek dan badan email
print ("Selamat datang!")
print ("--Kirim email 'Quotes Of The Day' secara cepat lewat sini.--")
fromaddr = str(input("Masukkan alamat email pengirim : "))
toaddr = str(input("Masukkan alamat email penerima : "))
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Quotes of The Day"
 
body = "'The illiterate of the 21st century will not be those who cannot read and write, but those who cannot learn, unlearn, and relearn.' ― Alvin Toffler"
print ("Email telah terkirim")
msg.attach(MIMEText(body, 'plain'))

# Lampiran
filename = "alvin-toffler.jpg"
attachment = open("C:\\Users\\user\\AI\\Final Project\\alvin-toffler.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

#Mengirim email melalui server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "21Jan2000")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


#Sumber koding & referensi pembelajaran : https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/