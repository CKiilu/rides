from rauth import OAuth2Service
import requests
import simplejson

from django.http import HttpResponse
from django.shortcuts import render, redirect

# from uber_rides.auth import AuthorizationCodeGrant
# from uber_rides.client import UberRidesClient
# from uber_rides.session import Session

# Create your views here.

CLIENT_ID = 'X9jVFhJ0fmllaplxIuSaiQWLQy4xN6Wz'
CLIENT_SECRET = '4B_lqZJ0F3EptF1zsh4U4VsE2g5XofecKaW_70FJ'
PERMISSION_SCOPES = [
    'profile',
    'ride_widgets',
    'history',
    'places',
    ]
REDIRECT_URL = 'https://rides-ckiilu.c9users.io/profile'
SERVER_TOKEN = '41ti1oAYb5wcLWKTUjgxG-B4grRYeYQlrVzoTCkf'

# Redirect user here to authorize your application


def home(request):
    uber_api = OAuth2Service(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        name='FuelMonitor',
        authorize_url='https://login.uber.com/oauth/authorize',
        access_token_url='https://login.uber.com/oauth/token',
        base_url='https://api.uber.com/v1/',
    )
    
    parameters = {
        'response_type': 'code',
        'redirect_uri': REDIRECT_URL,
        'scopes': PERMISSION_SCOPES,
    }
    login_url = uber_api.get_authorize_url(**parameters)
    context = {
        'login': login_url,
    }
    return render(request, 'home.html', context)
    
def profile(request):
    data = None
    if request.GET.get('code'):
        parameters = {
            'redirect_uri': REDIRECT_URL,
            'code': request.GET.get('code'),
            'grant_type': 'authorization_code',
        }
        
        response = requests.post(
            'https://login.uber.com/oauth/token',
            auth=(
                CLIENT_ID,
                CLIENT_SECRET,
            ),
            data=parameters,
        )
        access_token = response.json().get('access_token')
        url = 'https://api.uber.com/v1/me'
        response = requests.get(
            url,
            headers={
                'Authorization': 'Bearer %s' % access_token
            }
        )
        data = response.json()
    
    context = {
        'profile': data
    }
    return render(request, 'detail.html', context)
    
def coords(request):
    if request.is_ajax():
        req_type = request.GET.get('type')
        if req_type == 'time' or req_type == 'price':
            PARAMETERS = {
                'server_token': SERVER_TOKEN,
                'start_latitude': request.GET.get('start[lat]'),
                'end_latitude': request.GET.get('end[lat]'),
                'start_longitude': request.GET.get('start[lng]'),
                'end_longitude': request.GET.get('end[lat]'),
            }
            
            url = 'https://api.uber.com/v1/estimates/time' if req_type == 'time' else 'https://api.uber.com/v1/estimates/price'
        elif req_type == 'products':
            PARAMETERS = {
                'server_token': SERVER_TOKEN,
                'latitude': request.GET.get('end[lat]'),
                'longitude': request.GET.get('end[lng]'),
            }
            url = 'https://api.uber.com/v1/products'
        response = requests.get(url, params=PARAMETERS)
        print req_type
        data = response.text
        json = simplejson.dumps(data)
        return HttpResponse(json, 'application/json')