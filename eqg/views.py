from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from eqg.models import Datasets

def home(req):
    ds = Datasets.objects.all()
    return render(req, 'index.html', dict(datasets=ds))
        #return HttpResponse('Hello')

def new_dataset(req):
    name = req.POST.get('name')
    Datasets.objects.create(name=name)
    return HttpResponseRedirect('/')
