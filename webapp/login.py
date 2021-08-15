import web
import pyrebase 
 

firebaseConfig = {
    "apiKey": "AIzaSyBrsLDSfHmXNkLJzDda7SHMnoyVQQr_s5c",
    "authDomain": "dockerwebapp-6dec7.firebaseapp.com",
    "databaseURL": "https://dockerwebapp-6dec7-default-rtdb.firebaseio.com",
    "projectId": "dockerwebapp-6dec7",
    "storageBucket": "dockerwebapp-6dec7.appspot.com",
    "messagingSenderId": "910674893594",
    "appId": "1:910674893594:web:605b9aeaa34962f9e82aa3"
  }




render = web.template.render('templates/')

class Login():
    def GET(self):
        return render.login()

    def POST(self):
        try:
          firebase=pyrebase.initialize_app(firebaseConfig)
          auth=firebase.auth()
          i = web.input()
          email=i.email
          password=i.password
          auth.sign_in_with_email_and_password(email,password)
          return render.index()
        except Exception as error:
          print("Ups :{}".format(error.args[1]))
          return render.login()