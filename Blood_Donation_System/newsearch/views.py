from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from .models import Hospital


def index(request):
    all_hospitals = Hospital.objects.all()
    for hospital in all_hospitals:
        url = 'details/' + str(hospital.hospital_id) + '/'
        hospital.url = url
    return render(request, 'newsearch/Search.html', {'all_hospitals': all_hospitals})


def details(request, hospital_id):
    try:
        hospital = Hospital.objects.get(hospital_id=hospital_id)
    except Hospital.DoesNotExist:
        raise Http404("This hospital does not exist")
    return render(request, 'newsearch/details.html', context={'hospital': hospital})


def search(request):
    template = 'newsearch/details.html'

    query = request.GET.get('q')

    results = Hospital.objects.filter(Q(name__icontains=query) | Q(type__icontains=query))

    pages = 0
