from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from overwatch import Overwatch

overwatch = "ow"
league = "lol"

# Create your views here.
@login_required
def index(request):
    return render(request, 'games/index.html')

@login_required
def link_account(request, game, api_required_info):
    if request.user.is_authenticated:
        data = {}
        if game == overwatch:
            try:
                profile = Overwatch(battletag=api_required_info["battletag"])
            except:
                print("invalid credentials")
                return redirect('/games')
        return render(request, 'games/{}.html'.format(game))
    return redirect('/accounts/login')