from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from app.models import Players, Teams, Games

# Create your views here.
def index(request):
    # this is your new view
    if request.GET.get("grandpasays"):
        context = {
            "post": request.GET.get("grandpasays")
        }
    else:
        context = {
            "post": "nothing here yet!"
        }
    return render(request, 'index.html', context)
    
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST['password']
        
        # check if username exists
        user = User.objects.filter(username = username)
        if user:
            return redirect('home')    
        # if it exists:
            #print username is already existed
        else:
            user = User.objects.create(username = username, password = password)
            player = Players.objects.create_player(user=user)
            player.user = user
            player.save()
            user = authenticate(username = username, password = password)
            login(request, user)
    return redirect('personality_test')
    
def personality_test(request):
    user = request.user
    player = Players.objects.get(user_id = user.id) 
    return render(request, 'personality_test.html', {})
    
def submit(request):
    pass
    