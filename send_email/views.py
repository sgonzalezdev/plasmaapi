"""
-Title:  PlasmaAPI Customized Views (Methods)
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
    
    return render(request,'index.html',{'title':'PlasmaAPI'})

def reqs(request):
    
    return render(request,'reqs.html')

def installation(request):
     
    return render(request,'installation.html')

def release_notes(request):
   
    return render(request,'release_notes.html')
def example(request):
   
    return render(request,'example.html')

#Default email template look and feel.
def show_email_template(request):

  return render(request,'default_email_template.html')

@csrf_exempt
#This function submits the JSON object received thru the REST-API
def send_email(request, *args, **kwargs):
  
        message = {}
        if request.method == 'POST':
            # The message is received as a JSON from the REST-API, then, converted into an JSON object. 
            message = json.loads(request.body)
            #Let's split our object per fields.
            user_name = message['user_name']
            user_email=  message['user_email']
            user_subject =  message['user_reason']
            user_phone =  message['user_phone']
            user_message =  message['user_message']
            user_contact_via = message['user_contact_via'] 
            #Default incoming app_title
            app_title="Website"
            #Loading HTML Template
            html_content = render_to_string('default_email_template.html',{'title':'PlasmaAPI default_email_template.','content':user_message,'app_title':app_title,'phone':user_phone,'contact_via':user_contact_via,'user_email':user_email})
            text_content = strip_tags(html_content)
        #Note this is a Build-In django feature for sending emails in Django.

        #The function will recieve , Subject, Messsage and From 
            email = EmailMultiAlternatives(
                user_subject,
                text_content,
                user_email,
                ['sgonzalezdev@gmail.com']

            )
            email.attach_alternative(html_content,'text/html')
            email.send()
        return HttpResponse(message,content_type='text/json')

 


 
 