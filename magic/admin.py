from django.contrib import admin
from .models import User, Card, Collection
# import each model

# Register your models here.
admin.site.register(User)
admin.site.register(Card)
admin.site.register(Collection)
# make the admin aware of your model to render it