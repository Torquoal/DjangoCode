# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request): 							    #view function for homepage
	return HttpResponse("Hello World <br/><a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("About Rango <br/><a href='/rango'>Index</a>")