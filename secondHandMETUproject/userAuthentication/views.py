#authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from .models import UserProfile
from .forms import UserProfileForm

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
    return render(request, 'userAuthentication/dashboard.html', {'user_profile': user_profile})

#def search_results(request):
    # Implement your search functionality here
    # You can use request.GET.get('query') to get the search query from the URL parameters
    # Perform the search and prepare the data to be displayed
    # return render(request, 'userAuthentication/search_results.html', {'results': search_results_data})
    # Pass the data to the template and render it

    #return render(request, 'userAuthentication/search_results.html')