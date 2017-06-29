# from lib import rotate_string, do_passwords_match, is_string, reg, do_passwords_and_username_match, no_field_blank, passwords_length
from flask import Flask, request, url_for, render_template #, redirect
from lib import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/color", methods=['POST', 'GET'])
def color():
    """."""
    return render_template('color.html')

@app.route("/sound", methods=['POST', 'GET'])
def sound():
    """."""
    return render_template('sound.html')

@app.route("/sounds", methods=['POST', 'GET'])
def sounds():
    """."""
    return render_template('sounds.html')

@app.route("/")
def index():
    """Create a linkable page for all routes."""
    return render_template('links.html')

@app.route("/encrypt", methods=['POST', 'GET'])
def encrypt():
    """ie hitting submit querry over and over and both urls below work
    http://localhost:5000/encrypt # defaults to 1, a
    http://localhost:5000/encrypt?rot=3&text=p can be clicked again and again """
    if request.method == 'POST': # or  elif request.form:
        result_text = request.form['result_text']
        result_rot = int(request.form['result_rot'])
    if request.args:
        result_text = request.args.get('result_text')
        result_rot = int(request.args.get('result_rot'))
    else:
        result_text = ''
        result_rot = ''
    result_text = rotate_string(result_text, result_rot)
    result_rot = result_rot
    # option 1: just render result, not form
    # return result
    # option 2
    return render_template('encrypt.html', result_text=result_text, result_rot=result_rot)

# @app.route("/signup", methods=['POST', 'GET'])
@app.route("/signup", methods=['GET'])
# def signup(error='', username_error='', password_error='', email_error='', verify_error=''):
def signup(error='', username='', password='', verify='', email='', username_error='',
           password_error='', email_error='', verify_error=''):
            # def signup(username=None, password=None, verify=None, email=None):
    """ie hitting submit querry over and over and both urls below work
    http://localhost:5000/encrypt # defaults to 1, a
    http://localhost:5000/encrypt?rot=3&text=p can be clicked again and again """

    if request.args:
        username = request.args.get('username')
        password = request.args.get('password')
        verify = request.args.get('verify')
        email = request.args.get('email')
        # password = int(request.args.get('password'))
    else: # first time user hits page don't validate blank form
        return render_template('signup.html',
                        username=username, password=password, verify=verify,
                        email=email, error=error, username_error=username_error,
                        password_error=password_error, email_error=email_error,
                        verify_error=verify_error)

    # Validation Section
    if not usersname_length(username):
        username_error = 'Must be between 3 to 20 characters'

    if not do_passwords_match(password, verify): # False
        verify_error = 'Passwords must match'

    if do_passwords_and_username_match(username, password): # False
        password_error = 'Passwords cannot match username'

    if not passwords_length(password): # False
        password_error = 'Passwords must be at least 8 characters'

    # check string valitity
    for i in [username, password, verify, email]:
        if not is_string(i):
            error = 'Not a valid string'
            i = ''

    # provide optional param of email and use regex to check validity
    if not reg(email) and email != '':
        email_error = 'Must use a valid email'

    # when posted     if request.method == 'POST': # or  elif request.form:
    if error or username_error or password_error or email_error or verify_error:
        return render_template('signup.html',
                               username=username, password=password, verify=verify,
                               email=email, error=error, username_error=username_error,
                               password_error=password_error, email_error=email_error,
                               verify_error=verify_error)

    # if no_field_blank(username, password, verify): # False
    #     username_error = 'Must not leave any field blank (email optional)'

    else: # success
        # return render_template('welcome.html') # works without
        return render_template('welcome.html', username=username) # works with name
        # return signup_post(username=username) # ? ValueError: View function did not return a response
        # return prac() # works

@app.route("/prac", methods=['POST'])
def prac(error='', username='', password='', verify='', email='', username_error='',
           password_error='', email_error='', verify_error=''):
        return '<h1>hi</h1>'

@app.route("/signup", methods=['POST'])
def signup_post(error='', username_error='', password_error='', email_error='', verify_error=''):
# def signup_post(error='', username='', password='', verify='', email='', username_error='',
        #    password_error='', email_error='', verify_error=''):
    # SECTION NOT REQUIRED
    if request.method == 'POST': # or  elif request.form:
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
    return render_template('welcome.html', username=username)

# disable browser caching
@app.after_request
def add_header(response):
    """Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
#################################################################
if __name__ == '__main__':
    app.run()
