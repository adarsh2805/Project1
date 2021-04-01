from django.http import HttpResponse
import os
a=os.path.abspath(__file__)
b=os.path.dirname(os.path.dirname(a))


def index(request):
    c=os.path.join(b,'sample.html')
    file1=open(c,"r")
    a=file1.read()
    return HttpResponse(a)