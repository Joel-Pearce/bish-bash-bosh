from django.shortcuts import render, get_object_or_404
from .models import Challenges
from .forms import InputForm
from .functions import *
import os


def Challenge(request, challenge_id):
    challenge = get_object_or_404(Challenges, pk=challenge_id)
    if request.method == 'GET':
        return render(request, 'challenges/challenge.html', {'challenge': challenge, 'form': InputForm()})
    else:
        form = InputForm(request.POST)
        print(form.data['challenge_input'])
        print(type(form.data['challenge_input']))
        message = assign_challenge(form.data['challenge_input'], challenge_id)
        return render(request, 'challenges/challenge.html', {'challenge': challenge, 'form': form, 'message': message})
    
    








    
