from django.shortcuts import render
from datetime import datetime

def myworld(request):
    return render(request,"myfirst.html",{"today":datetime.today()})

# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())