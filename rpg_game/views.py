from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from rpg_game.models import Character, Item, Character_class
from rpg_game.forms import CreateCharacterForm


def index(request):
    return render_to_response("login.html")

def home(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect("play_game.html")
        elif not request.user.is_authenticated():
            return HttpResponse("LOGIN FIRST !")

def register(request):
    if request.method == 'GET':
        return render_to_response('register.html',
                                  {'form' : RegistrationForm()},
                                  context_instance=RequestContext(request))

    form = RegistrationForm(request.POST)
    if form.is_valid():
        user_data = {}
        user_data['username'] = form.cleaned_data['username']
        user_data['password'] = form.cleaned_data['password1']
        user_data['email'] = form.cleaned_data['email']
        user = User.objects.create_user(**user_data)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        user = authenticate(username=user_data['username'], password=user_data['password'])
        login(request, user)
        return render_to_response('/welcome.html')

    return render_to_response('register.html',
                              {'form' : form})

@login_required
def edit_profile(request):
    if request.method == 'GET':
        user = request.user
        return render_to_response('edit_profile.html',
                                  {'form' : EditProfileForm(instance=user)},
                                  context_instance=RequestContext(request))

    form = EditProfileForm(request.POST)
    if form.is_valid():
        user = request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        return redirect('/')

    return render_to_response('edit_profile.html',
                              {'form' : form})

@login_required
def play_game(request):
    user = request.user
    if request.method == 'GET':
        return render_to_response('play_game.html',{'form' : CreateCharacterForm(user=request.user)}, context_instance=RequestContext(request))

    form = CreateCharacterForm(request.POST)
    if form.is_valid():
        character_data = form.cleaned_data
        character_data['owner'] = request.user
        
        character = character(**character_data)
        character.save()
        return redirect('/rpg_game/characters')

def add_char(request):
    return render_to_response('add_character.html', {'form' : form}, context_instance=RequestContext(request))
