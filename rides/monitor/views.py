import requests
import simplejson

from django.http import HttpResponse
from django.shortcuts import render 

# from uber_rides.auth import AuthorizationCodeGrant
# from uber_rides.client import UberRidesClient
# from uber_rides.session import Session

# Create your views here.

CLIENT_ID = 'X9jVFhJ0fmllaplxIuSaiQWLQy4xN6Wz'
CLIENT_SECRET = '4B_lqZJ0F3EptF1zsh4U4VsE2g5XofecKaW_70FJ'
PERMISSION_SCOPES = [
    'profile',
    ]
REDIRECT_URL = 'https://rides-ckiilu.c9users.io'
SERVER_TOKEN = '41ti1oAYb5wcLWKTUjgxG-B4grRYeYQlrVzoTCkf'

def home(request):
    return render(request, 'home.html')
    
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