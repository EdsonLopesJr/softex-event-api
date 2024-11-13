from django.urls import path
from . import views

urlpatterns = [
   path('events/', view=views.events_list),
   path('event/', view=views.event_create)
]
