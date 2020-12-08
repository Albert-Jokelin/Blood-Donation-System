from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from .models import Hospital


def index(request):
    all_hospitals = Hospital.objects.all()
    for hospital in all_hospitals:
        url = 'details/' + str(hospital.hospital_id) + '/'
        hospital.url = url
    context = {'all_hospitals': all_hospitals}
    if request.GET:
        query = request.GET['q']
        results = search(query)
        context = {'query': results}
        return render(request, 'newsearch/SearchResults.html', context)

    return render(request, 'newsearch/Search.html', context)


def details(request, hospital_id):
    try:
        hospital = Hospital.objects.get(hospital_id=hospital_id)
    except Hospital.DoesNotExist:
        raise Http404("This hospital does not exist")
    return render(request, 'newsearch/details.html', context={'hospital': hospital})


def search(query=None):
    # query = request.GET.get('q')
    query_set = []
    queries = query.split(" ") # Create a set of words with space as delimiter

    for q in queries:
        posts = Hospital.objects.filter(
            Q(name__icontains=q)).distinct()

        for post in posts:
            query_set.append(post)
    return list(set(query_set))
