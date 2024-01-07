from fastapi import FastAPI, Depends
from authlib.integrations.starlette_client import OAuth

app = FastAPI()

oauth = OAuth()

oauth.register(
    name='google',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    authorize_prompt=None,
    authorize_response=None,
    token_url='https://accounts.google.com/o/oauth2/token',
    token_params=None,
    client_kwargs={'scope': 'openid profile email'},
)

@app.route('/login')
async def login(request):
    redirect_uri = url_for('auth', _external=True)
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.route('/auth')
async def auth(request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)
    return user
