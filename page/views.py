from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FILMS, ACTEURS
from .forms import FILM, FormActor
from django.template import loader




def index(request):
    form = FILM(request.POST or None)
    form_actor = FormActor(request.POST or None)
    context = {
        'form': form,
        'form_actor': form_actor,
    }
    return render(request, 'index.html', context )

# def listing(request): views.send_actor
#     films = ["<li>{}</li".format(film['name']) for film in FILMS]
#     message = """<ul>{}</ul>""".format("\n".join(films))
#     return HttpResponse(message)

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
        actor = ACTEURS(nom=8000)
        

        actor.save()


    return redirect( 'index')


def display_movie(request):
    temp = []
    list_movie = FILMS.objects.all()
    

    for film in list_movie:
        temp.append(film.nom)
    print(temp)  

    context = { 
        'temp': temp,
    }
    return render(request, 'film.html', context)

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
    return render(request, 'op.html')
    