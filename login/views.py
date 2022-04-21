import requests
from flask import redirect, request, current_app
from login import login_blue
from utils import get_header

authorize_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
login_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
graph_url = 'https://graph.microsoft.com/v1.0/'


@login_blue.route('/')
def login():
    client_id = current_app.config.get('CLIENT_ID')
    redirect_uri = current_app.config.get('REDIRECT_URI')
    scopes = current_app.config.get('SCOPES')
    return redirect(
        authorize_url + f"?client_id={client_id}&scope={scopes}&redirect_uri={redirect_uri}&response_type=code")


@login_blue.route('/redirect')
def login_redirect():
    code = request.args.get('code')
    get_token(code)
    get_drive()
    return {}


def get_token(code):
    client_id = current_app.config.get('CLIENT_ID')
    client_secret = current_app.config.get('CLIENT_SECRET')
    redirect_uri = current_app.config.get('REDIRECT_URI')
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    response = requests.post(login_url, data=params)
    body = response.json()
    current_app.config['ACCESS_TOKEN'] = body.get('access_token')
    current_app.config['REFRESH_TOKEN'] = body.get('refresh_token')


@login_blue.route('/refresh')
def get_refresh_token(refresh_token):
    client_id = current_app.config.get('CLIENT_ID')
    client_secret = current_app.config.get('CLIENT_SECRET')
    redirect_uri = current_app.config.get('REDIRECT_URI')
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "redirect_uri": redirect_uri,
        "grant_type": "refresh_token"
    }
    response = requests.post(login_url, data=params)
    return response.json()


def get_drive():
    path = "me/drive"
    response = requests.get(graph_url + path, headers=get_header())
    body = response.json()
    current_app.config['DRIVE_ID'] = body.get('id')
