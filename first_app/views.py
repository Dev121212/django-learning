from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    print(date_dict['access_records'][0])
    return render(request, 'first_app/index.html', context=date_dict)
