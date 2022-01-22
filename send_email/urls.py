
""" 
App (send_email) Urls 
-Title: Set Customized Urls
-Details: This will storages all urls from the app: send_email
-Version: 0.1.0
-Autor: Sergio Enmanuel González
"""

from pathlib import Path
from django.urls import path 
from . import views


#Let's creates the customized urls within app(send_email).
urlpatterns = [
    path('',views.index),
    path('send',views.send_email),
    path('<str:email_from>',views.send_email),

]
