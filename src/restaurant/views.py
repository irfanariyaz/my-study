# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	html_="""<!doctype html>
    <html lang="en">

    <head> 
    </head>
    <body>
    <h1>hello world</h1>
    <p>This is  aahhsh</p>
    </body>
    </html>"""
	return HttpResponse(html_)