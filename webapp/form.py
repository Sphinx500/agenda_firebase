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

class Form():
    def GET(self):
        return render.form()

def POST(self):
      try:
        firebase=pyrebase.initialize_app(firebaseConfig)
        f = web.input()
        nombre=f.nombre
        email=f.email
        database = firebase.database()
        data = {"nombre":nombre,"email":email}
        database.push(data)
        return render.agenda()
      except Exception as error:
        print("Ups :{}".format(error.args[1]))
        return render.login()