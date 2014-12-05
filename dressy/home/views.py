from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response



def home(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('home/index.html', context_dict, context)

