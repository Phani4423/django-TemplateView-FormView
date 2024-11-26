from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import TemplateView,FormView

# Create your views here.
def display(request):
    FD = StudentForm()
    d = {'FD':FD}
    if request.method == 'POST':
        FD = StudentForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('done')
        else:
            return HttpResponse('faild validation')
    return render(request,'display.html',d)
class RenderHTML(TemplateView):
    template_name = 'RenderHTML.html'
    def get_context_data(self,**kwargs):
        EDOC = super().get_context_data(**kwargs)
        EDOC['num'] = 5
        EDOC['form'] = StudentForm()
        
        return EDOC
    def post(self,request):
        if request.method == 'POST':
            PF = StudentForm(request.POST)
            if PF.is_valid():
                PF.save()
                return HttpResponse('Form submitted successfully')
            else:
                return HttpResponse('Form submission failed')
class Formview(FormView):
    template_name = 'FormView.html'
    form_class = StudentForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('Done')