from django.shortcuts import render , redirect
from .forms import ImageForm
from django.contrib import messages 
# Create your views here.

def index(request):
    if request.method == 'POST':
        form=ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'your image added successfullly')
            return redirect('home')
    else:      
        f=ImageForm()
        return render(request, 'index.html' ,{'form':f})
