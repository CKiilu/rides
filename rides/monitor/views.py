import requests

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

ESIMATE_PARAMETERS = {
    'server_token': SERVER_TOKEN,
    'start_latitude': 37.775818,
    'end_latitude': 37.775818,
    'start_longitude': 37.418028,
    'end_longitude': 37.975818,
}
PRODUCT_PARAMETERS = {
    'server_token': SERVER_TOKEN,
    'latitude': 37.775818,
    'longitude': -122.418028,
}

# Endpoints

price_estimate = 'https://api.uber.com/v1/estimates/price'
products = 'https://api.uber.com/v1/products'
time_estimate = 'https://api.uber.com/v1/estimates/time'

def home(request):
    response = requests.get(products, params=PRODUCT_PARAMETERS)
    context = {
        'uber_response': response.json(),
    }
    return render(request, 'home.html', context)