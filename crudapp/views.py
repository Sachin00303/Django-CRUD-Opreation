from django.shortcuts import render,redirect
from .models import Employee,fileupload
from django.views import View

from .form import empform
from .models import Employee

#from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
class ragisterView(CreateView):
    model=Employee
    form_class=empform
    template_name="index.html"
    success_url="/Showlist/"

from django.views.generic.edit import UpdateView
class updatempview(UpdateView):
    model=Employee
    form_class=empform
    template_name='update.html'
    success_url="/Showlist/"

from django.views.generic.edit import DeleteView
class ModelDeleteView(DeleteView):
    model = Employee
    template_name = "Employee_confirm_delete.html"
    success_url="/Showlist/"


from django.views.generic.list import ListView
class showListView(ListView):
    template_name='datalist.html'
    model=Employee
    context_object_name="data"
   
from django.views.generic.detail import DetailView   
class ModelDetailView(DetailView):
    model = Employee
    template_name = "details.html"


import pandas as pd
def upload(request):
    if request.method=="POST":
        name=request.POST.get('name')
        obj=fileupload(filename=name, file=request.FILES['fileUpload'])
        obj.save()
        filepath=obj.file.path
        print(filepath)
        df=pd.read_excel(filepath)
        bulk_list=[]
        for re in df.values:
            obj=Employee(empname=re[0] ,empemail=re[1] , empcontact=re[2],empcity=re[3] ,empsal=re[4])
            bulk_list.append(obj)
        print(bulk_list)
        objs=Employee.objects.bulk_create(bulk_list)
        return redirect("showdata")
    return render(request,"fileupload.html")