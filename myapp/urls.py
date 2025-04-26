from django.urls  import path
from .views import *

#login messages contact about 
urlpatterns = [
    path('home/', home, name='home'),
]
