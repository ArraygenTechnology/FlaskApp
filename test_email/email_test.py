from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bioinformatics.arraygen.ak@gmail.com'
app.config['MAIL_PASSWORD'] = 'arraygen123$'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_ASCII_ATTACHMENTS'] = True

mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'bioinformatics.arraygen.ak@gmail.com', recipients = ['akshata@arraygene.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   with app.open_resource("avatar.png") as fp:
      msg.attach("avatar.png", "image/png", fp.read())
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)