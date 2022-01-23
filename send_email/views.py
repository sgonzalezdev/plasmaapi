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

#This will be used for sending HTML e-mail Template customized message.
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# This function returns the main or index page. 
def index(request):
    #response = json.dumps([{}])
    return render(request,'index.html')

@csrf_exempt
#This function submits the JSON object received thru the REST-API
def send_email(request, *args, **kwargs):
  
        message = {}
        if request.method == 'POST':
            # The message is received as a JSON from the REST-API, then, converted into an JSON object. 
            message = json.loads(request.body)
            print(message)
            #Let's split our object per fields.
            user_name = message['user_name']
            print(user_name)
            user_email=  message['user_email']
            user_reason =  message['user_reason']
            user_phone =  message['user_phone']
            user_message =  message['user_message']
            user_contact_via = message['user_contact_via'] 
            #Loading HTML Template
            html_content = render_to_string('email_template.html',{'title':'test email','content':user_message})
            text_content = strip_tags(html_content)
            print(text_content)
        #Note this is a Build-In django feature for sending emails: send_mail()
            email = EmailMultiAlternatives(
                user_reason,
                text_content,
                user_email,
                ['sgonzalezdev@gmail.com']

            )
            email.attach_alternative(html_content,'text/html')
            email.send()
        return HttpResponse(message,content_type='text/json')
 