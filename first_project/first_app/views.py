from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body> My First Django Project <br><h3>Now time is %s.</h3></body></html>" % now
    return HttpResponse(html)
