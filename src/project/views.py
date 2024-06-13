from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisits

def return_view(request, *args, **kwargs):
    total_ps = PageVisits.objects.all()
    queryset = PageVisits.objects.filter(path=request.path)
    my_context = {
        'page':154865,
        'total_page_visit':total_ps.count(),
        'queryset':queryset.count()
    }
    PageVisits.objects.create(path=request.path)

    return render(request, 'home.html', context=my_context)