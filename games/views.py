from django.http import HttpResponse
from django.shortcuts import render

def game(request):
	return HttpResponse("Hello Games Logged in?:{}".format(not request.user.is_anonymous))
