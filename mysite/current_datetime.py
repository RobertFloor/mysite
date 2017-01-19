#from django.template.loader import get_template
from django.shortcuts import render
#from django.template import Context
#from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date':now})
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)