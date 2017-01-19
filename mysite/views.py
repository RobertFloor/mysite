from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    try:
        ua = request.META['REMOTE_ADDR']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Hello world, you are visiting %s, %s" % (request.path, ua ))
    
def meta_data(request):
    meta = request.META.items()
    html=[]
    for key, value in meta:
        html.append('<tr><td>%s</td><td>%s</td></tr>)' % (key,value)) 
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    


def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s) it wille be %s." % (offset, dt)
    return render(request, 'hours_ahead.html', {'hour_offset':offset, 'next_time':dt})