from django.shortcuts import render,redirect
from .models import Item
from .forms import SellItemForm
from userAuthentication.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import formset_factory

# Create your views here.
@login_required
def sell_item(request):
    if request.method == 'POST':
        form = SellItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('userAuthentication:dashboard')
    else:
        form = SellItemForm()

    return render(request, 'marketplace/sell_item.html', {'form': form})

def my_posts(request):
    user_posts = Item.objects.filter(user=request.user)
    return render(request, 'marketplace/my_posts.html', {'user_posts': user_posts})