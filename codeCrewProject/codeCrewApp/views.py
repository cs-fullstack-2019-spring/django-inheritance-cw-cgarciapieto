from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

# renders the index page
def index(request):
    return render(request,'codeCrewApp/index.html')
# renders the about us page
def aboutus(request):
    return render(request,'codeCrewApp/aboutus.html')

# renders the gallery page
def gallery(request):
    return render(request,'codeCrewApp/gallery.html')

# renders resources page
def resources(request):
    return render(request,'codeCrewApp/resources.html')

# renders the contact us page obtains a GET request from the form model, than saves users input and inputs it the data base
def contactus(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    return render(request,'codeCrewApp/contactus.html',{"form":form})

