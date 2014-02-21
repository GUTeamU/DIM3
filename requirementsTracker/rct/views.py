from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def login(request):
	context = RequestContext(request)
	context_dict ={'boldmessage': "BOLD"}
	return render_to_response('rct/login.html',context_dict,context)