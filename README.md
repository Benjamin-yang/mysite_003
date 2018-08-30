# Django 重定向
### HttpResponseRedirect 和 reverse 联系构成
## 1, HttpResponse, render 和 HttpResponseRedirect

    from django.shortcuts import render, redirect
    from django.http import HttpResponse, HttpResponseRedirect
    from django.core.urlresolvers import reverse
    from . import models
     
    def index(request):
     
        context = models.user.objects.all()
        return render(request, 'mydata/index.html', {'context': context})
     
    def add(request):
     
        username = request.POST['username']
        pwd = request.POST['pwd']
     
        models.user.objects.create(username=username, pwd=pwd)
     
        # return HttpResponseRedirect('/mydata/index/')
        # redirect('mydata:index')
     
        return HttpResponseRedirect('/mydata/index/')
   