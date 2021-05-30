'''
Created on 01-Jan-2018

@author: ashwani
'''
from django.urls.conf import path
from . import views

app_name = 'swp'
urlpatterns = [
    path('handling/', views.handle_audio, name='handling')

]