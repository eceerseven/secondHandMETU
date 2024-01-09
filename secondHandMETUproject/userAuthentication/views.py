#userAuthentication/views.py
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from .models import UserProfile
from .forms import UserProfileForm

from .forms import ItemSearchForm
from requests_aws4auth import AWS4Auth
from django.middleware import csrf

import requests


#from retrying import retry
#from urllib3.util import Retry
#from requests.adapters import HTTPAdapter

@login_required
def user_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('userAuthentication:dashboard')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'userAuthentication/user_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            #Creating user profile
            UserProfile.objects.create(user=user, bio='', profile_picture='default.jpg')  # Add default values

            login(request, user)
            return redirect('home')  #Redirecting to home page
    else:
        form = UserCreationForm()
    return render(request, 'userAuthentication/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('userAuthentication:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'userAuthentication/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')  #Redirecting home page


def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    search_results = []

    if request.method == 'GET':
        search_form = ItemSearchForm(request.GET)
        if search_form.is_valid():
            search_query = search_form.cleaned_data.get('query', '')

            # AWS CloudSearch configuration

            aws_access_key_id = '**********'
            aws_secret_access_key = '****************'

            aws_region = 'us-east-1'
            cloudsearch_domain = 'secondhand'

            # Constructing the CloudSearch endpoint
            cloudsearch_endpoint = 'https://search-secondhand-maq5eq722nglglhjt4fxvwiyuy.us-east-1.cloudsearch.amazonaws.com'
            # Creating AWS4Auth object
            aws_auth = AWS4Auth(aws_access_key_id, aws_secret_access_key, aws_region, 'cloudsearch')
            csrf_token = csrf.get_token(request)
            # Including CSRF token in headers
            headers = {'X-CSRFToken': csrf_token}
            # Requesting
            url = f'{cloudsearch_endpoint}/2013-01-01/search?q={search_query}&return=item_name,description,image,condition,price'
            response = requests.get(url, auth=aws_auth)

            # Checking if the request was successful
            if response.status_code == 200:
                # Extracting search results as needed
                search_results = response.json().get('hits', {}).get('hit', [])
            else:
                print(f"Error performing CloudSearch: {response.status_code} - {response.text}")

    return render(request, 'userAuthentication/dashboard.html', {'user_profile': user_profile, 'search_results': search_results, 'search_form': search_form})

