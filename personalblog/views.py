from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def post1(request):
    return render(request, "post1.html")