from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.flatpages.models import FlatPage
# Create your views here.


def index(request):
    home = get_object_or_404(FlatPage, url__exact='/home/')
    return render_to_response("simple.html", {'object': home, },
                              context_instance=RequestContext(request))


def disclaimer(request):
    obj = FlatPage.objects.get(url__exect='/disclaimer/')
    return render_to_response('simple.html', {'object': obj, },
                              context_instance=RequestContext(request))


def static_path(request):
    return HttpResponse('static folder: ' + 'to be announced')
