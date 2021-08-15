import web
import index
import form

urls = (
    '/index', 'index.Index',
    '/form', 'form.Form',
    '/','login.Login'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()