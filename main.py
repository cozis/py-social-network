from flask import Flask, request, abort, redirect
from flask_login import LoginManager, login_user, logout_user
import flask_login

categories = {
       'Informatica': 'Qui i post di informatica',
    'Programmazione': '..e qui di programmazione'
}

users = { 'cozis': 'hello', 'haru': 'python' }

def create_user(username, password):
    if username in users:
        return False # Already exists OwO
    users[username] = password 

def user_exists(username, password=None):
    
    x = (username in users)
    
    if password is None:
        return x
    
    return x and users[username] == password

class User(flask_login.UserMixin):
    pass

app = Flask(__name__)
app.secret_key = 'super secret string'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return

    user = User()
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in users:
        return

    user = User()
    user.id = username
    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401

@app.errorhandler(404)
def not_found(error):
    return "page not found"

@app.route('/logout', methods=['GET'])
def logout():
    # TODO: Destroy the session.
    logout_user()
    return redirect("/login", code=303)

@app.route('/categories', methods=['GET'])
def list_categories():
    content = str(list(categories.keys()))
    return f'''
    <html>
        <head></head>
        <body>
            <nav>
                [<a href="/logout">Esci</a>]
            </nav>
            {content}
        </body>
    </html>
    '''

@app.route('/',      methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        if user_exists(username, password):
            u = User()
            u.id = username
            login_user(u)
            return redirect("/categories", code=303)
        
        error = 'There\'s no such user' 

    return f'''<html>
    <head></head>
    <body>
        <nav>
            [<a href="/">Entra</a>]
            [<a href="/signup">Iscriviti</a>]
        </nav>
        <h1>ENTRA ORA</h1>
        <p>{error}</p>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="[Username]" />
            <br />
            <br />
            <input type="password" name="password" placeholder="[Password]" />
            <br />
            <br />
            <input type="submit" value="Log-in" />
        </form>
    </body>
</html>'''

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ''
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        
        try:
            if create_user(database, username, password):
                return redirect("/categories", code=303)
            
            error = 'Bad data'
        except:
            error ='Internal error'

    return f'''<html>
    <head></head>
    <body>
        <nav>
            [<a href="/">Entra</a>]
            [<a href="/signup">Iscriviti</a>]
        </nav>
        <h1>REGISTRATI ORA</h1>
        <p>{error}</p>
        <form action="/signup" method="POST">
            <input type="text" name="username" placeholder="[Username]" />
            <br />
            <br />
            <input type="password" name="password" placeholder="[Password]" />
            <br />
            <br />
            <input type="submit" value="Log-in" />
        </form>
    </body>
</html>'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)