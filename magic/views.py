from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CardForm
from .models import Card

# Create your views here.
# This is where actions happen. They are triggered by the user (or an AJAX request with JS) visiting a url. 


def index(request):
    cards = Card.objects.filter(owner=request.user)
    # context will be data from the database
    form = CardForm()
    context = {
        'form': form,
        'cards': cards
    }

    return render(request, 'magic/index.html', context)


def create_card(request):
    if request.method == 'POST':
        # if the form was submitted
        form = CardForm(request.POST)
        # this form is 'bound', meaning it is populated with data that the user entered
        if form.is_valid():
            # checks if the data from the form can actually be saved in the db without error
            card = form.save(commit=False)
            # commit is false to hold off on putting data in db until additional info added
            card.owner = request.user
            card.save()
                # saves new instance of Card in the db

            # builds a blank card form to render on the page if the user visits the page initially (GET)
            data = {
                'created': 'yes',
                'card_title': card.name,
                'card_owner': card.owner.username
            }
        else:
            data = {
                'errors': form.errors
            }
    else:
        data = {
            'response': "you can't do that here"
        }
    # update HTTPResponse to be a JsonResponse since user will not be visiting this url, just requests from JS
    return JsonResponse(data)
