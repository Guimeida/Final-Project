from flask import Flask, render_template, session, request, redirect
import pyrebase

app = Flask(__name__)
config = {
    'apiKey': "AIzaSyDALm7gnIuvtIE5cWjl3ALjfLKqP3901co",
    'authDomain': "final-project-dd90a.firebaseapp.com",
    'projectId': "final-project-dd90a",
    'storageBucket': "final-project-dd90a.appspot.com",
    'messagingSenderId': "533375267682",
    'appId': "1:533375267682:web:3d2ae3335fa51ffdbf323b",
    'measurementId': "G-7HR3RG82M3",
    'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get("login")
        register = request.form.get("signup")
        if login is not None:
            email = request.form.get('email')
            password = request.form.get('pswd')
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                user_id = user['idToken']
                session['usr'] = user_id
            except:
                return 'Failed to login'
            return render_template('inicio.html')
        elif register is not None:
            email = request.form.get('email')
            password = request.form.get('pswd')
            try:
                new_user = auth.create_user_with_email_and_password(email, password)
            except:
                return 'Failed to create new user'
            return render_template('inicio.html')
    else:
        return render_template('start.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('start.html')

if __name__ == '__main__':
    app.run(port=1111)

@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/etc')
def etc():
    return render_template('etc.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')



