from django.shortcuts import render


def about_page(request):
    """ A view to return the home page """
    return render(request, 'about/about.html')
