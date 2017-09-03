from django.http import HttpResponse
from django.shortcuts import render

def landing(request):
	return HttpResponse("Hello Landing! Logged in?:{}".format(not request.user.is_anonymous))
