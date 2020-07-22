from django.shortcuts import render

# Create your views here.


def home_page(request):
    """ A view to return the home page """
    return render(request, 'home/index.html')
