from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=40)
    email_id = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
  	
    def __str__(self):
        return self.username + " " + self.password

		
class Purpose(models.Model):
    purpose_of_visit = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=40)
    tenth = models.CharField(max_length=40)
    twelth = models.CharField(max_length=40)
    graduate = models.CharField(max_length=40)
    stream = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    visa_date_applied = models.CharField(max_length=40)
    visa_date_recieved = models.CharField(max_length=40)
    college = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    

class Subscriber(models.Model):
    daily_alerts = models.CharField(max_length=40)
    
class Enquiry(models.Model):
    fullname = models.CharField(max_length=40)
    contact = models.CharField(max_length=40)
    visa_type = models.CharField(max_length=40)
