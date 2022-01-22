"""
App (send_email) Views
-Title:  Customized Views (Methods)
-Details: This contains all methods that will render a view in the app (send_email)
-Version: 0.1.0
-Autor: Sergio Enmanuel González
"""


from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail

import json
from .models import Messages
# This is the main page.


def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


# This will receive a JSON Object, then, submit it thru email.
"""def  show_email(request, email_from):
    response = []
    if request.method =='GET':
        response = [{'user_name':'test','user_email':'webmail@testcom'}]
       # try:
       #    message = Messages.objects.get(user_email=email_from)
        #   response = json.dumps([{'user_name':message.user_name, 'user_message':message.user_message}])
       # except:
          # response = json.dumps([{ 'error':'Not found'}])

    return HttpResponse(response,content_type='text/json') """


@csrf_exempt
def send_email(request, email_from):

    if request.method == 'POST':

        message = json.loads(request.body)
        user_name = message['user_name']
        user_email=  message ['user_email']
        user_reason =  message ['user_reason']
        user_phone =  message ['user_phone']
        user_message =  message ['user_message']
        user_contact_via = message ['user_contact_via'] 
        save_message = Messages( user_name =  user_name ,user_email= user_email,user_reason = user_reason,user_phone =  user_phone,user_message = user_message,user_contact_via = user_contact_via)
    #build-in django feacture for sending emails.
        send_mail(
            user_reason,
            user_message,
            user_email,
            ['sgonzalezdev@gmail.com'],
            fail_silently=False,
        )

        try:
           save_message.save()
           response = json.dumps([{'message':'Added.'}])
        except:
            response = json.dumps([{ 'error':'Could not add.'}])
    else:
        message = [{'user_name':'test','user_email':'webmail@testcom'}]
        # try:
        #    message = Messages.objects.get(user_email=email_from)
        #   response = json.dumps([{'user_name':message.user_name, 'user_message':message.user_message}])
        # except:
        #   response = json.dumps([{ 'error':'Not found'}])
           
    return HttpResponse(message,content_type='text/json')
 