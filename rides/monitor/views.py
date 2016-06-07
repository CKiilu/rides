from rauth import OAuth2Service
import requests
import simplejson

from django.core.cache import cache
from django.core.urlresolvers import reverse
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
    'request',
    ]
HISTORY_REDIRECT_URL = 'https://rides-ckiilu.c9users.io/history'
PAY_REDIRECT_URL = 'https://rides-ckiilu.c9users.io/pay_method'
PROFILE_REDIRECT_URL = 'https://rides-ckiilu.c9users.io/profile'
SERVER_TOKEN = '41ti1oAYb5wcLWKTUjgxG-B4grRYeYQlrVzoTCkf'
test_url ="https://sandbox-api.uber.com/v1/"
prod_url = 'https://api.uber.com/v1/',

uber_api = OAuth2Service(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    name='FuelMonitor',
    authorize_url='https://login.uber.com/oauth/authorize',
    access_token_url='https://login.uber.com/oauth/token',
    base_url=test_url
)

# Redirect user here to authorize your application


def home(request):
    pay_parameters = {
        'response_type': 'code',
        'redirect_uri': PAY_REDIRECT_URL,
        'scopes': PERMISSION_SCOPES,
    }
    prof_parameters = {
        'response_type': 'code',
        'redirect_uri': PROFILE_REDIRECT_URL,
        'scopes': PERMISSION_SCOPES,
    }
    hist_parameters = {
        'response_type': 'code',
        'redirect_uri': HISTORY_REDIRECT_URL,
        'scopes': PERMISSION_SCOPES,
    }
    pay_url = uber_api.get_authorize_url(**pay_parameters)
    prof_url = uber_api.get_authorize_url(**prof_parameters)
    hist_url = uber_api.get_authorize_url(**hist_parameters)
    
    context = {
        'profile': prof_url,
        'history': hist_url,
        'pay': pay_url,
    }
    return render(request, 'home.html', context)
    
def profile(request):
    data = None
    if request.GET.get('code'):
        data = uber_auth(request, test_url + 'me', PROFILE_REDIRECT_URL)
    context = {
        'profile': data,
    }
    return render(request, 'detail.html', context)
    
    
def pay_method(request):
    data = None
    if request.GET.get('code'):
        data = uber_auth(request, test_url + 'payment-methods', PAY_REDIRECT_URL)
    context = {
        'pay': data,
    }
    return render(request, 'history.html', context)
    
def history(request):
    data = None
    if request.GET.get('code'):
        data = uber_auth(request, test_url[:len(test_url) - 1] + '.2/history', HISTORY_REDIRECT_URL)
    
    context = {
        'history': data
    }
    return render(request, 'history.html', context)
    
def uber_auth(request, url, redirected_url):
    parameters = {
        'redirect_uri': redirected_url,
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
    response = requests.get(
        url,
        headers={
            'Authorization': 'Bearer %s' % access_token
        }
    )
    
    return response.json()
        
    
def coords(request):
    if request.is_ajax():
        req_type = request.GET.get('type')
        if req_type == 'time' or req_type == 'price':
            PARAMETERS = {
                'server_token': SERVER_TOKEN,
                'start_latitude': request.GET.get('start[lat]'),
                'end_latitude': request.GET.get('end[lat]'),
                'start_longitude': request.GET.get('start[lng]'),
                'end_longitude': request.GET.get('end[lng]'),
            }
            
            
            url = 'estimates/time' if req_type == 'time' else 'estimates/price'
        elif req_type == 'products':
            PARAMETERS = {
                'server_token': SERVER_TOKEN,
                'latitude': request.GET.get('end[lat]'),
                'longitude': request.GET.get('end[lng]'),
            }
            url = 'products'
        response = requests.get(test_url + url, params=PARAMETERS)
        data = response.text
        json = simplejson.dumps(data)
        return HttpResponse(json, 'application/json')