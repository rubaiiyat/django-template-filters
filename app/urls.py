from django.urls import path
from .import views
urlpatterns = [
    path('templates/',views.templates),
    path('about/',views.about),
    path('contact/',views.contact),
]
