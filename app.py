################################   imports   ###################################
from flask import Flask, render_template, request, session, url_for


##############################   applicaio   ###################################
app = Flask(__name__)

################################   pagines   ###################################
@app.route('/', methods=['POST', 'GET'])
def index():
    clean_sesion()
    return render_template('index.html')

@app.route('/home',methods=['POST', 'GET'])
def hola():
    if request.method == 'POST':
        save_sesion()
        if valid_login(session['user'], session['pass']): return render_template('home.html', nom=session['user'] , con=session['pass'])
        else: return render_template('home_e.html')
    else:
        return render_template('home_e.html')

###############################   funcions   ##################################
def valid_login(a, b):
    ## FUTURA IMPLEMENTACIO AMB BASE DE DADES
    if a == 'a' and b=='b': return True
    else: return False

def save_sesion():
    session['user'] = request.form['user']
    session['pass'] = request.form['pass']
    return

def clean_sesion():
    session['user'] = ''
    session['pass'] = ''
    return
#xd

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host="localhost", debug=True, port=80)
