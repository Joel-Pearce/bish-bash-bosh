from django.shortcuts import render
from .models import Challenges
from .forms import InputForm
from .functions import challenge1_tests
import os


def Challenge(request):
    challenges = Challenges.objects.all()
    if request.method == 'GET':
        return render(request, 'challenges/challenge.html', {'challenges': challenges, 'form': InputForm()})
    else:
        form = InputForm(request.POST)
        message = challenge1_tests(form.data['challenge_input'])
        return render(request, 'challenges/challenge.html', {'challenges': challenges, 'form': form, 'message': message})


    
