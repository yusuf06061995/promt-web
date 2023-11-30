from django.shortcuts import render 
# Create your views here.


def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,'about.html')


def query_form(request):
    return render(request, 'queryform.html')


def support(request):
    return render(request,'support.html')

def testimonial(request):
    return render(request,'testimonial.html')

def team(request):
    return  render(request,'team.html')


def page_not_found(request, exception):
    return render(request, 'page-404.html')


def under_maintenance(request):
    return render(request,'under-maintenance.html')
    


