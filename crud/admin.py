from django.contrib import admin
from .models import User, Purpose, Subscriber, Enquiry

# Register your models here.
admin.site.register(User)
admin.site.register(Purpose)
admin.site.register(Subscriber)
admin.site.register(Enquiry)
