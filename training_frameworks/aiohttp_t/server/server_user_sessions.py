'''Module for testing of user sessions'''
import time
import datetime
import base64
from aiohttp import web
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet


async def main(request):
    '''This is main function for main page'''
    session = await get_session(request)
    print(session)
    last_visit = session['last_visit'] if 'last_visit' in session else None
    text = f'Last visited: {last_visit}'
    session['last_visit'] = f'{str(time.time())} - {str(datetime.datetime.now())}'
    return web.Response(text=text)

async def make_app():
    '''Function for making our app'''
    app = web.Application()

    fernter_key = fernet.Fernet.generate_key()
    print(fernter_key)
    secret_key = base64.urlsafe_b64decode(fernter_key)
    print(secret_key)
    setup(app, EncryptedCookieStorage(secret_key))
    app.add_routes([web.get('/', main)])
    return app


if __name__ == '__main__':
    web.run_app(make_app())
