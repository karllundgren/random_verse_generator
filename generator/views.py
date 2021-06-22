from django.shortcuts import render
from .constants import *
from .forms import *
from .random_verse import getScripture
#import sys


# Create your views here.
def index(request):
    volume = ""
    result = ""
    form = DetermineVolumeForm(request.POST)
    
    if request.method == 'POST':
        method = "POST"        
        if form.is_valid():
            print("form is VALID")
            volume = request.POST['volume']
            print("volume of Scripture: " + volume)
            result = getScripture(volume)

        else:
            print("form is INVALID")
            print(form.errors)
    elif request.method == 'GET':
        result = getScripture(allScriptures)

    #print("result length:" + str(len(result)))
    if len(result) > 0:
        context = {
            "volume" : result[6],
            "verse_reference" : result[3],
            "verse_text" : result[4],
            "link_to_verse" : result[5],
        }
    else:
        context = {
        }
    return render(
        request,
        'index.html',
        context

    )


def display_verse(request, pk):
    
    if request.method == 'POST':
        form = DetermineVolumeForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            volume = form.cleaned_data['volume']
            
            # More to go here


    # If this is a GET (or any other method) create the default form.
    else:
        print("seems to be a GET")

    context = {
    }

    return render(request, 'index.html', context)