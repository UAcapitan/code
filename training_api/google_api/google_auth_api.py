from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

GOOGLE_SCOPES = 'https://www.googleapis.com/auth/userinfo.email',
GOOGLE_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_USER_INFO_URI = 'https://www.googleapis.com/oauth2/v1/userinfo'

GOOGLE_CLIENT_ID = '584434119467-futqefiguil1kejhaeptjqiujhgmrc8o.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_REDIRECT_URI = 'http://127.0.0.1:5000/'

parametrs = {
    'redirect_uri': GOOGLE_REDIRECT_URI,
    'response_type': 'code',
    'client_id': GOOGLE_CLIENT_ID,
    'scope' : GOOGLE_SCOPES[0],
}

url = GOOGLE_AUTH_URI + '?'

for i,j in parametrs.items():
    url += i+'='+j+'&'

print(url[:-1:])

if __name__ == '__main__':
    app.run(debug=True)