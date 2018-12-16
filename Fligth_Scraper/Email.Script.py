import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "flylafel.code@gmail.com"
toaddr = "molle4boltz@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Check out your cheap flights"

body = " Hello lucky stranger. \n" \
       "This is your lovely flylafel team. We want to let you know that you could by flights to palma for " \
       "less then your falafel around the corner.\n " \
       "Come check us out under flylafel.com to see more of our crazy deals."
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "billig123")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()