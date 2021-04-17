from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
import requests


CLIENT_ID = 'cBis5C5Gz6XmHp6d1eb1xPOlzzLKhT6tOIXknvnz'
CLIENT_SECRET = '3oJarOoTqVV6FRJ2jkiKgBs15RV26X6eJ42LPZGYec3CtdMtNz79ONLtw2x13dYgOlLwSryXYPLPTdI3XlqZWXcJ6d9L2QGGUDaxkXOdFqpp6Tvll5yhwy6Tm3J7hN7l'


IP_token = 'http://10.61.64.58:8000/o/token/'
IP_revoke_token = 'http://10.61.64.58:8000/o/revoke_token/'

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/posts/')
    else:
        f = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': f})


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    r = requests.post(
        IP_token,
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    r = requests.post(
        IP_token,
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    r = requests.post(
        IP_revoke_token,
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    return Response(r.json(), r.status_code)
