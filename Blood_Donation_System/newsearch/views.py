from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Hospital


def index(request):
    all_hospitals = Hospital.objects.all()

    context = {
        'all_hospitals': all_hospitals,
    }
    return render(request, 'newsearch/Search.html', context)

#def other():
 #   html = ''
  #  for bloodbanks in all_bloodbanks:
   #     url = '/bloodbanks/' + str(bloodbanks.id) + '/'

# Create your views here.
