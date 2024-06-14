from django.shortcuts import render
from .models import PageVisits

# Create your views here.

def return_view(request):
    PageVisits.objects.create()
    page_count =  PageVisits.objects.all()
    
    page = {
        'page':page_count.count()
    }

    return render(request, 'home.html', context=page)