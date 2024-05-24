from django.shortcuts import render,HttpResponse
from .models import Message

def index(request):

    message = Message.objects.first() 
    
    if message:
        # If a message exists, render it in the template
        return render(request, 'world/index.html', {'message': message})
    else:
        # If no message exists, return a simple HttpResponse
        return HttpResponse("No message found in the database")


