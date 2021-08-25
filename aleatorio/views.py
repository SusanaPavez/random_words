from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):

    request.session['counter'] = 0

    context = {
        'word':   get_random_string(length=14)
    }

    return render(request, 'index.html', context)




def random_word(request):

    if 'counter' in request.session:

        request.session['counter'] = request.session['counter'] + 1

    else:

        request.session['counter'] = 0


    context = {
        'word':   get_random_string(length=14)
    }
    return render(request, 'index.html', context)




def reset(request):

    if request.session['counter']:

        del request.session['counter']
        
    return redirect('/')
