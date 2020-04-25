from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PhotoForm
from myapp.main import main

class MyappView(TemplateView):
    def __init__(self):
        self.params={'pred1': 'idx1',
                     'pred2':'idx2',
                     'pred3':'idx3',
                     'form': PhotoForm()}
    def get(self, req):
        return render(req, 'myapp/index.html', self.params)

    def post(self, req):
        form = PhotoForm(req.POST, req.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')
        
        image = form.cleaned_data['image']
        self.params['pred1'] = main(image)[0]
        self.params['pred2'] = main(image)[1]
        self.params['pred3'] = main(image)[2]
        return render(req, 'myapp/index.html', self.params)