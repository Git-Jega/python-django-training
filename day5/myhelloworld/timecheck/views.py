from django.shortcuts import render
from datetime import datetime
# Create your views here.
def timecheck(request):
  return render(request,"timecheck.html",{"today":datetime.today})
