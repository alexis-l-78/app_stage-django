from django.urls import path


from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('send_datas/', views.send_datas, name='send_datas'),
    path('send_actor/', views.send_actor, name='send_actor'),
    path('display_movie/', views.display_movie, name='display_movie'),
    path('search/', views.search, name='search'),
    path('search_film/', views.search_film, name='search_film'),
    path('op/', views.op, name='op'),
]