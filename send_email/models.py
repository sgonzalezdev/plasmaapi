from django.db import models

# Create your models here.
class Messages(models.Model):
        user_name = models.CharField(max_length=200, null=False)
        user_email= models.EmailField(max_length=254, default='webmail@sgonzalezdev.com')
        user_reason = models.TextField( null=False)
        user_phone = models.CharField(max_length=20, null=False)
        user_message = models.TextField( null=False)
        user_contact_via = models.CharField(max_length=10, null=False)