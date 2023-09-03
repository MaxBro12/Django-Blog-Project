from django.shortcuts import render


# Create your views here.
def index(request):
    return render()


def about(request):
    return render(request, 'main/about.html', context={'title': 'О нас'})
