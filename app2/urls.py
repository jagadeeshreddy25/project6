from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('rusell/',rusell,name='rusell'),
]