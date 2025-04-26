from django.urls  import path
from .views import *

#login messages contact about 
urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('messages/', my_messages, name='messages'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
