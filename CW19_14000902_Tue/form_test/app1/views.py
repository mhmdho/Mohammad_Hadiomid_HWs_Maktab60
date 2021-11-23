from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

# Create your views here.


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        print(request.POST)
        print(form.is_valid)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()
    
    return render(request, "name.html", {"form":form})
