from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def home(request):
   if request.method=='POST':
      data=(request.POST)
      name=data['name']
      email=data['email']
      message=data['message']

      user=Student(name=name,email=email,message=message)
      user.save()
      return HttpResponse('Submitted Successfully!!')
   return render(request, 'home.html')
