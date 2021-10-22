GOOGLE_SCOPES = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]
GOOGLE_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_USER_INFO_URI = 'https://www.googleapis.com/oauth2/v1/userinfo'

GOOGLE_CLIENT_ID = '584434119467-cnga0vkfsu38iugu671u5ar371p2dt29.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_REDIRECT_URI = 'http://edmix.ua/callback.py'

parametrs = {
    'redirect_uri': GOOGLE_REDIRECT_URI,
    'response_type': 'code',
    'client_id': GOOGLE_CLIENT_ID,
    'scope' : ' '.join(GOOGLE_SCOPES),
}