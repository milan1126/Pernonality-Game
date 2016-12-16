from django.shortcuts import render, redirect

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
    
def login(request):
    if request.method == 'POST':
        post = request.POST["post-data"]
        if post == post.upper():
            return redirect("/?grandpasays=HI GRANDPA!Red Necks Suck!")
        elif post == post.lower():    
            return redirect("/?grandpasays=What? I can't hear you Sonny!")
        else:
            return redirect("/?grandpasays=Hey Dude!")