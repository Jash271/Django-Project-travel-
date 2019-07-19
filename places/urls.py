from django.urls import include, path
from . import views

urlpatterns = [
    path("place",views.place,name='place'),
    path("destination",views.det,name='det'),
    path("user",views.register,name='register'),
    path("book",views.book,name='book'),
 
]
