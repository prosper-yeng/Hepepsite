# from django.shortcuts import render_to_response
from django.shortcuts import render
from .models import HepepsTeam, BackgroundImages,Services,Blog



# Create your views here.
def home(request):
    all_team = HepepsTeam.objects.all()
    bgimages = BackgroundImages.objects.all()
    service=Services.objects.all()

    return render(request, 'accounts/index.html', {'all_team': all_team,'bgimages': bgimages,'service':service})


def bgimages(request):
    imgs = BackgroundImages.objects.all()
    return render(request, 'accounts/index.html', {'imgs': imgs})


# services function
def services(request):
    service = Services.objects.all()
    return render(request, 'accounts/services.html',{'service':service})


# blog function
def blog(request):
    bg=Blog.objects.all()
    return render(request, 'accounts/blog.html',{'bg':bg})


# portfolio function
def portfolio(request):
    return render(request, 'accounts/portfolio.html')


# contact function
def contact(request):
    return render(request, 'accounts/contact.html')
