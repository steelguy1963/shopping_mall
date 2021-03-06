from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from users.forms import ProfileForm
from users.models import Profile
# Create your views here.

def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, 'list.html')
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def editProfile(request):
    profile = None
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = None
    form = ProfileForm(request.POST or None, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'registration/profile.html', {'form':form})