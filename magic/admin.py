from django.contrib import admin
from .models import User, Card
# import each model

# Register your models here.
admin.site.register(User)
admin.site.register(Card)
# make the admin aware of your model to render it