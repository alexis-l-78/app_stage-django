from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FILMS, Actor
from .forms import FILM, FormActor, NewUserForm, NouveauContactForm
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


def index(request):
    form = FILM(request.POST or None)
    form_actor = FormActor(request.POST or None)
    context = {
        'form': form,
        'form_actor': form_actor,
    }
    return render(request, 'index.html', context )


def send_datas(request):

    form = FILM(request.POST or None)

    if request.method == 'POST':

        name=request.POST["film"]
        # FILMS.objects.create(nom=name)
        film = FILMS(nom=name)
        

        film.save()


    return redirect( 'index')


def send_actor(request):

    form_actor = FormActor(request.POST or None)

    if request.method == 'POST':
        
        name=request.POST["actor"]

        name=str(name)

        name = name.lower()
        # FILMS.objects.create(nom=name)
        actor = Actor(nom=8000)
        

        actor.save()


    return redirect( 'index')



def search(request):
    form = FILM(request.POST or None)
    context= {
        'form':form
    }
    return render(request, 'search.html', context)



def search_film(request):
    form = FILM(request.POST or None)

    query = request.GET.get('film')

    films = FILMS.objects.filter(nom__icontains=query)
    
    if not films:
        message = "Nous n'avons pas trouvé votre film, désolé "
        return HttpResponse(message)




    context = { 
        'films':films,
        'form':form
    }
    return render(request, 'search.html', context)
 
def op(request):
    temp = []
    list_movie = FILMS.objects.all()
    

    for film in list_movie:
        temp.append(film.nom)

    context = { 
        'temp': temp,
    }
    return render(request, 'op.html', context)

def logout_request(request):
    if request.method == "GET":
        logout(request)
        print('PASS')
        messages.info(request, "Logged out succesfully !")
        return redirect('/')

def register(request):
    if request.method == "POST":
        form_register = UserCreationForm(request.POST)
        if form_register.is_valid():
            user = form_register.save()
            username = form_register.cleaned_data.get('username')
            messages.success(request, "New account created: {}".format(username))
            login(request, user)
            return redirect("/")
        
        else:
            for msg in form_register.error_messages:
                print(form_register.error_messages[msg])
            
            return render(request, 'register.html', context={"form_register":form_register})

    form_register = UserCreationForm
    return render(request, 'register.html', context={"form_register":form_register})

def login_request(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(request=request, data=request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'You are now logged in as {username}'.format(username))
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form_login = AuthenticationForm()
    return render(request, 'login.html', context={"form_login":form_login})

def contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'contact.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })