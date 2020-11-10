from django.http import HttpResponse
from django.template import loader
import Blood_Donation_System.System.models as model


def index(request):
    all_hospitals = model.Hospital.objects.all()
    template = loader.get_template('Search/Search.html')
    context = {
        'all_hospitals': all_hospitals,
    }
    return HttpResponse(template.render(context, request))

#def other():
 #   html = ''
  #  for bloodbanks in all_bloodbanks:
   #     url = '/bloodbanks/' + str(bloodbanks.id) + '/'