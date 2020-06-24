from django.urls import path


from . import views

urlpatterns = [ 
    path('', views.op, name='op'),
    path('index/', views.index, name="index"),
    path('send_datas/', views.send_datas, name='send_datas'),
    path('send_actor/', views.send_actor, name='send_actor'),
    path('search/', views.search, name='search'),
    path('search_film/', views.search_film, name='search_film'),
    path('register/', views.register, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout_request/', views.logout_request, name="logout_request"),
    path('contact/', views.contact, name="contact"),
]